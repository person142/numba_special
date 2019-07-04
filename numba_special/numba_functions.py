import ctypes

import numba
import scipy.special as sc

from . import function_pointers


signatures = {
    'gamma[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
}


def get_scalar_function(name):
    signature = signatures[name]
    pointer = function_pointers.functions[name]
    return signature(pointer)


@numba.extending.overload(sc.gamma)
def gamma(x):
    if isinstance(x, types.float64):
        return get_scalar_function('gamma[double]')
