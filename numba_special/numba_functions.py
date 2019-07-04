import ctypes

import numba
import scipy.special as sc

from . import function_pointers


signatures = {
    'gamma[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
}


@numba.extending.overload(sc.gamma)
def gamma(x):
    if isinstance(x, types.float64):
        signature = signatures['gamma[double]']
        pointer = function_pointers.functions['gamma[double]']
        return signature(pointer)
