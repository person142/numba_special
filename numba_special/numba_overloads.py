
import ctypes

import numba
import scipy.special as sc

from . import function_pointers


functions = {
    'cbrt': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'erf[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'erfc[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'erfcx[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'erfi[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'exp1[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'gamma[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
}


def get_scalar_function(name):
    signature = functions[name]
    pointer = function_pointers.functions[name]
    return signature(pointer)



@numba.extending.overload(sc.cbrt)
def cbrt(x):
    if x == numba.types.float64:
        f = get_scalar_function('cbrt')
        return lambda x: f(x)


@numba.extending.overload(sc.erf)
def erf(x):
    if x == numba.types.float64:
        f = get_scalar_function('erf[double]')
        return lambda x: f(x)


@numba.extending.overload(sc.erfc)
def erfc(x):
    if x == numba.types.float64:
        f = get_scalar_function('erfc[double]')
        return lambda x: f(x)


@numba.extending.overload(sc.erfcx)
def erfcx(x):
    if x == numba.types.float64:
        f = get_scalar_function('erfcx[double]')
        return lambda x: f(x)


@numba.extending.overload(sc.erfi)
def erfi(x):
    if x == numba.types.float64:
        f = get_scalar_function('erfi[double]')
        return lambda x: f(x)


@numba.extending.overload(sc.exp1)
def exp1(x):
    if x == numba.types.float64:
        f = get_scalar_function('exp1[double]')
        return lambda x: f(x)


@numba.extending.overload(sc.gamma)
def gamma(x):
    if x == numba.types.float64:
        f = get_scalar_function('gamma[double]')
        return lambda x: f(x)

