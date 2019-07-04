import ctypes

import numba
import scipy.special as sc

from . import function_pointers


signatures = {
    'gamma_double': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
}


def get_scalar_function(name):
    signature = signatures[name]
    pointer = function_pointers.functions[name]
    return signature(pointer)


@numba.extending.overload(sc.gamma)
def gamma(x):
    if x == numba.types.float64:
        f = get_scalar_function('gamma_double')
        return lambda x: f(x)
