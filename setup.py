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
    name='numba_special',
    description="Numba overloads for SciPy's special functions",
    version='0.1',
    author='Josh Wilson',
    url='https://github.com/person142/numba_special',
    packages=['numba_special'],
    package_data={'numba_special': ['signatures.json']},
    ext_modules = cythonize(EXT_MODULES),
    install_requires=['numba', 'scipy']
)
