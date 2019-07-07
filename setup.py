import os
from setuptools import setup, Extension
from Cython.Build import cythonize

EXT_MODULES = [
    Extension(
        'numba_special.function_pointers',
        [os.path.join('numba_special', 'function_pointers.pyx')]
    )
]


def get_long_description():
    readme = os.path.join(
        os.path.abspath(os.path.dirname(__file__)),
        'README.md'
    )
    with open(readme, encoding='utf-8') as f:
        long_description = f.read()
    return long_description


setup(
    name='numba_special',
    description="Numba overloads for SciPy's special functions",
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    version='0.1.0rc2',
    author='Josh Wilson',
    url='https://github.com/person142/numba_special',
    packages=['numba_special'],
    package_data={'numba_special': ['signatures.json']},
    ext_modules=cythonize(EXT_MODULES),
    install_requires=['cython', 'numba', 'scipy']
)
