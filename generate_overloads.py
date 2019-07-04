import os
import json

PWD = os.path.abspath(os.path.dirname(__file__))
MODULE = os.path.join(PWD, 'numba_special')

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


functions = {{
{FUNCTIONS}
}}


def get_scalar_function(name):
    signature = functions[name]
    pointer = function_pointers.functions[name]
    return signature(pointer)


{OVERLOADS}
"""

OVERLOAD_TEMPLATE = """
@numba.extending.overload(sc.{FUNCTION})
def {FUNCTION}(x):
    if x == numba.types.float64:
        f = get_scalar_function('{FUNCTION}_{TYPE}')
        return lambda x: f(x)
"""


def get_signatures():
    with open(os.path.join(PWD, 'signatures.json')) as f:
        signatures = json.load(f)
    return signatures


def generate_function_pointers(signatures):
    functions = []
    for name, specialization in signatures.items():
        for cython_key in specialization.keys():
            specialized_name = '{}_{}'.format(name, cython_key)
            cast = '<void *>sc.{}[{}]'.format(name, cython_key)
            functions.append("'{}': PyLong_FromVoidPtr({})".format(
                specialized_name, cast,
            ))

    functions = '    ' + ',\n    '.join(functions)
    content = FUNCTION_POINTERS_TEMPLATE.format(FUNCTIONS=functions)
    with open(os.path.join(MODULE, 'function_pointers.pyx'), 'w') as f:
        f.write(content)


def generate_numba_overloads(signatures):
    functions = []
    overloads = []
    for name, specialization in signatures.items():
        for cython_key, ctypes_signature in specialization.items():
            specialized_name = '{}_{}'.format(name, cython_key)
            ctypes_signature = [
                'ctypes.{}'.format(t) for t in ctypes_signature
            ]
            joined_ctypes = ', '.join(ctypes_signature)
            functions.append("'{}': ctypes.CFUNCTYPE({})".format(
                specialized_name, joined_ctypes,
            ))
            overloads.append(OVERLOAD_TEMPLATE.format(
                FUNCTION=name, TYPE=cython_key,
            ))

    functions = '    ' + ',\n    '.join(functions)
    overloads = '\n'.join(overloads)
    content = NUMBA_OVERLOADS_TEMPLATE.format(
        FUNCTIONS=functions, OVERLOADS=overloads,
    )
    with open(os.path.join(MODULE, 'numba_overloads.py'), 'w') as f:
        f.write(content)


def main():
    signatures = get_signatures()
    generate_function_pointers(signatures)
    generate_numba_overloads(signatures)


if __name__ == '__main__':
    main()
