import os
from distutils.core import setup, Extension
from Cython.Build import cythonize

EXT_MODULES = [
    Extension(
        'numba_special.function_pointers',
        [os.path.join('numba_special', 'function_pointers.pyx')]
    )
]

setup(
    ext_modules = cythonize(EXT_MODULES)
)
