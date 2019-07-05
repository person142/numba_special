
#cython: language_level=3
from cpython.long cimport PyLong_FromVoidPtr

cimport scipy.special.cython_special as sc


functions = {
    'cbrt': PyLong_FromVoidPtr(<void *>sc.cbrt),
    'erf[double]': PyLong_FromVoidPtr(<void *>sc.erf[double]),
    'erfc[double]': PyLong_FromVoidPtr(<void *>sc.erfc[double]),
    'erfcx[double]': PyLong_FromVoidPtr(<void *>sc.erfcx[double]),
    'erfi[double]': PyLong_FromVoidPtr(<void *>sc.erfi[double]),
    'exp1[double]': PyLong_FromVoidPtr(<void *>sc.exp1[double]),
    'gamma[double]': PyLong_FromVoidPtr(<void *>sc.gamma[double])
}
