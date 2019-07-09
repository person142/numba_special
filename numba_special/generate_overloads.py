import os
import json
import ctypes

PWD = os.path.abspath(os.path.dirname(__file__))

FUNCTION_POINTERS_TEMPLATE = """
#cython: language_level=3
from cpython.long cimport PyLong_FromVoidPtr

cimport scipy.special.cython_special as sc


functions = {{
{FUNCTIONS}
}}
"""

NUMBA_OVERLOADS_TEMPLATE = """
import ctypes

import numba
import scipy.special as sc

from . import function_pointers

bytes_to_int_type = {{
    2: numba.types.int16,
    4: numba.types.int32,
    8: numba.types.int64
}}

numba_long = bytes_to_int_type[ctypes.sizeof(ctypes.c_long)]

functions = {{
{FUNCTIONS}
}}


def get_scalar_function(name):
    signature = functions[name]
    pointer = function_pointers.functions[name]
    return signature(pointer)


{OVERLOADS}
"""

OVERLOAD_HEADER = """
@numba.extending.overload(sc.{FUNCTION})
def {FUNCTION}(*args):"""

OVERLOAD_BLOCK = """
    if args == {NUMBA_TYPES}:
        f = get_scalar_function('{SPECIALIZED_NAME}')
        return lambda *args: f(*args)
"""

INIT_TEMPLATE = '''"""
Available overloads
===================

The following variants of SciPy's special functions can be used inside
Numba jitted code. Arguments are specified by their Numba types except
for the C ``long`` type, where an equivalent Numba type does not
exist. To determine what Numba integer type ``long`` is on your
system, run::

  >>> import ctypes
  >>> 8 * ctypes.sizeof(ctypes.c_long)

Common values are ``int32`` and ``int64``.
{FUNCTIONS}
"""
from . import numba_overloads
'''


CTYPES_TO_NUMBA_TYPES = {
    'c_double': 'numba.types.float64',
    'c_long': 'numba_long'
}

CTYPES_TO_SHORT_NUMBA_TYPES = {
    'c_double': 'float64',
    'c_long': 'long'
}


def get_signatures():
    with open(os.path.join(PWD, 'signatures.json')) as f:
        signatures = json.load(f)
    return signatures


def get_specialized_name(name, cython_key):
    if cython_key == '':
        # Not a fused type function, so no need to specialize.
        return name

    cython_key = ', '.join(cython_key.split('|'))
    return '{}[{}]'.format(name, cython_key)


def generate_function_pointers(signatures):
    functions = []
    for name, specializations in signatures.items():
        for cython_key in specializations.keys():
            specialized_name = get_specialized_name(name, cython_key)
            cast = '<void *>sc.{}'.format(specialized_name)
            functions.append("'{}': PyLong_FromVoidPtr({})".format(
                specialized_name, cast,
            ))

    functions = '    ' + ',\n    '.join(functions)
    content = FUNCTION_POINTERS_TEMPLATE.format(FUNCTIONS=functions)
    with open(os.path.join(PWD, 'function_pointers.pyx'), 'w') as f:
        f.write(content)


def generate_overload(name, specializations):
    overload = OVERLOAD_HEADER.format(FUNCTION=name)
    for cython_key, ctypes_signature in specializations.items():
        ctypes_signature = ctypes_signature[1:]
        numba_types = (CTYPES_TO_NUMBA_TYPES[arg] for arg in ctypes_signature)
        specialized_name = get_specialized_name(name, cython_key)
        overload += OVERLOAD_BLOCK.format(
            NUMBA_TYPES='({},)'.format(', '.join(numba_types)),
            SPECIALIZED_NAME=specialized_name,
        )
    return overload


def generate_numba_overloads(signatures):
    functions = []
    overloads = []
    for name, specializations in signatures.items():
        for cython_key, ctypes_signature in specializations.items():
            specialized_name = get_specialized_name(name, cython_key)
            ctypes_signature = [
                'ctypes.{}'.format(t) for t in ctypes_signature
            ]
            joined_ctypes = ', '.join(ctypes_signature)
            functions.append("'{}': ctypes.CFUNCTYPE({})".format(
                specialized_name, joined_ctypes,
            ))

        overloads.append(generate_overload(name, specializations))

    functions = '    ' + ',\n    '.join(functions)
    overloads = '\n'.join(overloads)
    content = NUMBA_OVERLOADS_TEMPLATE.format(
        FUNCTIONS=functions, OVERLOADS=overloads,
    )
    with open(os.path.join(PWD, 'numba_overloads.py'), 'w') as f:
        f.write(content)


def generate_specialization_docstring_line(name, ctypes_signature):
    args = ', '.join(
        CTYPES_TO_SHORT_NUMBA_TYPES[arg]
        for arg in ctypes_signature[1:]
    )
    return '    {RETURN} {NAME}({ARGS})'.format(
        RETURN=CTYPES_TO_SHORT_NUMBA_TYPES[ctypes_signature[0]],
        NAME=name,
        ARGS=args,
    )


def generate_docstring_functions(signatures):
    functions = []
    for name, specializations in signatures.items():
        item = '\n- :data:`scipy.special.{}`::\n'.format(name)
        functions.append(item)
        for ctypes_signature in specializations.values():
            functions.append(generate_specialization_docstring_line(
                name, ctypes_signature
            ))
    return '\n'.join(functions)


def generate_init(signatures):
    functions = generate_docstring_functions(signatures)
    content = INIT_TEMPLATE.format(FUNCTIONS=functions)
    with open(os.path.join(PWD, '__init__.py'), 'w') as f:
        f.write(content)


def main():
    signatures = get_signatures()
    generate_function_pointers(signatures)
    generate_numba_overloads(signatures)
    generate_init(signatures)


if __name__ == '__main__':
    main()
