#cython: language_level=3
from cpython.long cimport PyLong_FromVoidPtr

cimport scipy.special.cython_special as sc


functions = {
    'gamma_double': PyLong_FromVoidPtr(<void *>sc.gamma[double])
}
