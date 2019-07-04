
#cython: language_level=3
from cpython.long cimport PyLong_FromVoidPtr

cimport scipy.special.cython_special as sc


functions = {
    'erf_double': PyLong_FromVoidPtr(<void *>sc.erf[double]),
    'erfc_double': PyLong_FromVoidPtr(<void *>sc.erfc[double]),
    'erfcx_double': PyLong_FromVoidPtr(<void *>sc.erfcx[double]),
    'erfi_double': PyLong_FromVoidPtr(<void *>sc.erfi[double]),
    'exp1_double': PyLong_FromVoidPtr(<void *>sc.exp1[double]),
    'gamma_double': PyLong_FromVoidPtr(<void *>sc.gamma[double]),
    'jv_double': PyLong_FromVoidPtr(<void *>sc.jv[double])
}
