
import ctypes

import numba
import scipy.special as sc

from . import function_pointers


functions = {
    'erf_double': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'erfc_double': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'erfcx_double': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'erfi_double': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'exp1_double': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'gamma_double': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
}


def get_scalar_function(name):
    signature = functions[name]
    pointer = function_pointers.functions[name]
    return signature(pointer)



@numba.extending.overload(sc.erf)
def erf(x):
    if x == numba.types.float64:
        f = get_scalar_function('erf_double')
        return lambda x: f(x)


@numba.extending.overload(sc.erfc)
def erfc(x):
    if x == numba.types.float64:
        f = get_scalar_function('erfc_double')
        return lambda x: f(x)


@numba.extending.overload(sc.erfcx)
def erfcx(x):
    if x == numba.types.float64:
        f = get_scalar_function('erfcx_double')
        return lambda x: f(x)


@numba.extending.overload(sc.erfi)
def erfi(x):
    if x == numba.types.float64:
        f = get_scalar_function('erfi_double')
        return lambda x: f(x)


@numba.extending.overload(sc.exp1)
def exp1(x):
    if x == numba.types.float64:
        f = get_scalar_function('exp1_double')
        return lambda x: f(x)


@numba.extending.overload(sc.gamma)
def gamma(x):
    if x == numba.types.float64:
        f = get_scalar_function('gamma_double')
        return lambda x: f(x)

