
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
    'gamma[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'j0': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'jv[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double)
}


def get_scalar_function(name):
    signature = functions[name]
    pointer = function_pointers.functions[name]
    return signature(pointer)



@numba.extending.overload(sc.cbrt)
def cbrt(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('cbrt')
        return lambda *args: f(*args)


@numba.extending.overload(sc.erf)
def erf(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('erf[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.erfc)
def erfc(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('erfc[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.erfcx)
def erfcx(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('erfcx[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.erfi)
def erfi(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('erfi[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.exp1)
def exp1(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('exp1[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gamma)
def gamma(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('gamma[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.j0)
def j0(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('j0')
        return lambda *args: f(*args)


@numba.extending.overload(sc.jv)
def jv(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('jv[double]')
        return lambda *args: f(*args)

