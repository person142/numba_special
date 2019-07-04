#cython: language_level=3
from cpython.long cimport PyLong_FromVoidPtr

cimport scipy.special.cython_special as sc


cdef function_pointer_to_long(void *p):
    res = PyLong_FromVoidPtr(p)
    if res == NULL:
        raise ValueError('Could not convert function address to int')
    return res


functions = {
    'gamma[double]': function_pointer_to_long(<void *>sc.gamma[double])
}
