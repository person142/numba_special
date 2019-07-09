
import ctypes

import numba
import scipy.special as sc

from . import function_pointers

bytes_to_int_type = {
    2: numba.types.int16,
    4: numba.types.int32,
    8: numba.types.int64
}

numba_long = bytes_to_int_type[ctypes.sizeof(ctypes.c_long)]

functions = {
    'agm': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'bdtr[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'bdtr[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_double),
    'bdtrc[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'bdtrc[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_double),
    'bdtri[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'bdtri[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_double),
    'bdtrik': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'bdtrin': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'bei': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'beip': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'ber': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'berp': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'besselpoly': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'beta': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'betainc': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'betaincinv': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'betaln': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'binom': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'boxcox': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'boxcox1p': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'btdtr': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'btdtri': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'btdtria': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'btdtrib': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'cbrt': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'chdtr': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'chdtrc': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'chdtri': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'chdtriv': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'chndtr': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'chndtridf': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'chndtrinc': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'chndtrix': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'cosdg': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'cosm1': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'cotdg': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'dawsn[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'ellipe': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'ellipeinc': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'ellipkinc': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'ellipkm1': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'entr': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'erf[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'erfc[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'erfcx[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'erfi[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'eval_chebyc[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_chebyc[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'eval_chebys[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_chebys[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'eval_chebyt[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_chebyt[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'eval_chebyu[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_chebyu[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'eval_gegenbauer[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_gegenbauer[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double, ctypes.c_double),
    'eval_genlaguerre[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_genlaguerre[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double, ctypes.c_double),
    'eval_hermite': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'eval_hermitenorm': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'eval_jacobi[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_jacobi[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_laguerre[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_laguerre[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'eval_legendre[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_legendre[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'eval_sh_chebyt[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_sh_chebyt[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'eval_sh_chebyu[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_sh_chebyu[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'eval_sh_jacobi[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_sh_jacobi[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_sh_legendre[double, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'eval_sh_legendre[long, double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'exp1[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'exp10': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'exp2': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'expi[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'expit[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'expm1[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'expn[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'expn[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'exprel': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'fdtr': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'fdtrc': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'fdtri': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'fdtridfd': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'gamma[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'gammainc': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'gammaincc': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'gammainccinv': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'gammaincinv': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'gammaln': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'gammasgn': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'gdtr': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'gdtrc': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'gdtria': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'gdtrib': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'gdtrix': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'huber': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'hyp0f1[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'hyp1f1[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'hyp2f1[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'hyperu': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'i0': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'i0e': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'i1': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'i1e': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'inv_boxcox': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'inv_boxcox1p': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'it2struve0': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'itmodstruve0': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'itstruve0': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'iv[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'ive[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'j0': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'j1': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'jv[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'jve[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'k0': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'k0e': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'k1': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'k1e': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'kei': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'keip': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'ker': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'kerp': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'kl_div': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'kn[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'kn[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'kolmogi': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'kolmogorov': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'kv[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'kve[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'log1p[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'log_ndtr[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'loggamma[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'logit[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'lpmv': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'mathieu_a': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'mathieu_b': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'modstruve': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'nbdtr[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'nbdtr[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_double),
    'nbdtrc[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'nbdtrc[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_double),
    'nbdtri[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'nbdtri[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_long, ctypes.c_double),
    'nbdtrik': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'nbdtrin': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'ncfdtr': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'ncfdtri': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'ncfdtridfd': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'ncfdtridfn': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'ncfdtrinc': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'nctdtr': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'nctdtridf': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'nctdtrinc': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'nctdtrit': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'ndtr[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'ndtri': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'nrdtrimn': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'nrdtrisd': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'obl_cv': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'owens_t': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'pdtr[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'pdtr[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'pdtrc[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'pdtrc[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'pdtri[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'pdtri[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'pdtrik': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'poch': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'pro_cv': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'pseudo_huber': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'psi[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'radian': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'rel_entr': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'rgamma[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'round': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'sindg': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'smirnov[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'smirnov[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'smirnovi[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'smirnovi[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'spence[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'stdtr': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'stdtridf': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'stdtrit': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'struve': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'tandg': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'tklmbda': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'xlog1py[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'xlogy[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'y0': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'y1': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double),
    'yn[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'yn[long]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_long, ctypes.c_double),
    'yv[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'yve[double]': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double, ctypes.c_double),
    'zetac': ctypes.CFUNCTYPE(ctypes.c_double, ctypes.c_double)
}


def get_scalar_function(name):
    signature = functions[name]
    pointer = function_pointers.functions[name]
    return signature(pointer)



@numba.extending.overload(sc.agm)
def agm(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('agm')
        return lambda *args: f(*args)


@numba.extending.overload(sc.bdtr)
def bdtr(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('bdtr[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba_long, numba.types.float64,):
        f = get_scalar_function('bdtr[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.bdtrc)
def bdtrc(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('bdtrc[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba_long, numba.types.float64,):
        f = get_scalar_function('bdtrc[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.bdtri)
def bdtri(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('bdtri[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba_long, numba.types.float64,):
        f = get_scalar_function('bdtri[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.bdtrik)
def bdtrik(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('bdtrik')
        return lambda *args: f(*args)


@numba.extending.overload(sc.bdtrin)
def bdtrin(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('bdtrin')
        return lambda *args: f(*args)


@numba.extending.overload(sc.bei)
def bei(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('bei')
        return lambda *args: f(*args)


@numba.extending.overload(sc.beip)
def beip(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('beip')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ber)
def ber(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('ber')
        return lambda *args: f(*args)


@numba.extending.overload(sc.berp)
def berp(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('berp')
        return lambda *args: f(*args)


@numba.extending.overload(sc.besselpoly)
def besselpoly(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('besselpoly')
        return lambda *args: f(*args)


@numba.extending.overload(sc.beta)
def beta(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('beta')
        return lambda *args: f(*args)


@numba.extending.overload(sc.betainc)
def betainc(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('betainc')
        return lambda *args: f(*args)


@numba.extending.overload(sc.betaincinv)
def betaincinv(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('betaincinv')
        return lambda *args: f(*args)


@numba.extending.overload(sc.betaln)
def betaln(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('betaln')
        return lambda *args: f(*args)


@numba.extending.overload(sc.binom)
def binom(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('binom')
        return lambda *args: f(*args)


@numba.extending.overload(sc.boxcox)
def boxcox(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('boxcox')
        return lambda *args: f(*args)


@numba.extending.overload(sc.boxcox1p)
def boxcox1p(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('boxcox1p')
        return lambda *args: f(*args)


@numba.extending.overload(sc.btdtr)
def btdtr(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('btdtr')
        return lambda *args: f(*args)


@numba.extending.overload(sc.btdtri)
def btdtri(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('btdtri')
        return lambda *args: f(*args)


@numba.extending.overload(sc.btdtria)
def btdtria(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('btdtria')
        return lambda *args: f(*args)


@numba.extending.overload(sc.btdtrib)
def btdtrib(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('btdtrib')
        return lambda *args: f(*args)


@numba.extending.overload(sc.cbrt)
def cbrt(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('cbrt')
        return lambda *args: f(*args)


@numba.extending.overload(sc.chdtr)
def chdtr(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('chdtr')
        return lambda *args: f(*args)


@numba.extending.overload(sc.chdtrc)
def chdtrc(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('chdtrc')
        return lambda *args: f(*args)


@numba.extending.overload(sc.chdtri)
def chdtri(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('chdtri')
        return lambda *args: f(*args)


@numba.extending.overload(sc.chdtriv)
def chdtriv(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('chdtriv')
        return lambda *args: f(*args)


@numba.extending.overload(sc.chndtr)
def chndtr(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('chndtr')
        return lambda *args: f(*args)


@numba.extending.overload(sc.chndtridf)
def chndtridf(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('chndtridf')
        return lambda *args: f(*args)


@numba.extending.overload(sc.chndtrinc)
def chndtrinc(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('chndtrinc')
        return lambda *args: f(*args)


@numba.extending.overload(sc.chndtrix)
def chndtrix(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('chndtrix')
        return lambda *args: f(*args)


@numba.extending.overload(sc.cosdg)
def cosdg(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('cosdg')
        return lambda *args: f(*args)


@numba.extending.overload(sc.cosm1)
def cosm1(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('cosm1')
        return lambda *args: f(*args)


@numba.extending.overload(sc.cotdg)
def cotdg(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('cotdg')
        return lambda *args: f(*args)


@numba.extending.overload(sc.dawsn)
def dawsn(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('dawsn[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ellipe)
def ellipe(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('ellipe')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ellipeinc)
def ellipeinc(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('ellipeinc')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ellipkinc)
def ellipkinc(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('ellipkinc')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ellipkm1)
def ellipkm1(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('ellipkm1')
        return lambda *args: f(*args)


@numba.extending.overload(sc.entr)
def entr(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('entr')
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


@numba.extending.overload(sc.eval_chebyc)
def eval_chebyc(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_chebyc[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('eval_chebyc[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_chebys)
def eval_chebys(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_chebys[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('eval_chebys[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_chebyt)
def eval_chebyt(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_chebyt[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('eval_chebyt[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_chebyu)
def eval_chebyu(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_chebyu[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('eval_chebyu[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_gegenbauer)
def eval_gegenbauer(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_gegenbauer[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_gegenbauer[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_genlaguerre)
def eval_genlaguerre(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_genlaguerre[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_genlaguerre[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_hermite)
def eval_hermite(*args):
    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('eval_hermite')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_hermitenorm)
def eval_hermitenorm(*args):
    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('eval_hermitenorm')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_jacobi)
def eval_jacobi(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_jacobi[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_jacobi[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_laguerre)
def eval_laguerre(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_laguerre[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('eval_laguerre[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_legendre)
def eval_legendre(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_legendre[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('eval_legendre[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_sh_chebyt)
def eval_sh_chebyt(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_sh_chebyt[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('eval_sh_chebyt[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_sh_chebyu)
def eval_sh_chebyu(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_sh_chebyu[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('eval_sh_chebyu[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_sh_jacobi)
def eval_sh_jacobi(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_sh_jacobi[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_sh_jacobi[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.eval_sh_legendre)
def eval_sh_legendre(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('eval_sh_legendre[double, double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('eval_sh_legendre[long, double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.exp1)
def exp1(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('exp1[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.exp10)
def exp10(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('exp10')
        return lambda *args: f(*args)


@numba.extending.overload(sc.exp2)
def exp2(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('exp2')
        return lambda *args: f(*args)


@numba.extending.overload(sc.expi)
def expi(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('expi[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.expit)
def expit(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('expit[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.expm1)
def expm1(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('expm1[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.expn)
def expn(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('expn[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('expn[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.exprel)
def exprel(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('exprel')
        return lambda *args: f(*args)


@numba.extending.overload(sc.fdtr)
def fdtr(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('fdtr')
        return lambda *args: f(*args)


@numba.extending.overload(sc.fdtrc)
def fdtrc(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('fdtrc')
        return lambda *args: f(*args)


@numba.extending.overload(sc.fdtri)
def fdtri(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('fdtri')
        return lambda *args: f(*args)


@numba.extending.overload(sc.fdtridfd)
def fdtridfd(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('fdtridfd')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gamma)
def gamma(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('gamma[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gammainc)
def gammainc(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('gammainc')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gammaincc)
def gammaincc(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('gammaincc')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gammainccinv)
def gammainccinv(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('gammainccinv')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gammaincinv)
def gammaincinv(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('gammaincinv')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gammaln)
def gammaln(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('gammaln')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gammasgn)
def gammasgn(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('gammasgn')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gdtr)
def gdtr(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('gdtr')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gdtrc)
def gdtrc(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('gdtrc')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gdtria)
def gdtria(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('gdtria')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gdtrib)
def gdtrib(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('gdtrib')
        return lambda *args: f(*args)


@numba.extending.overload(sc.gdtrix)
def gdtrix(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('gdtrix')
        return lambda *args: f(*args)


@numba.extending.overload(sc.huber)
def huber(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('huber')
        return lambda *args: f(*args)


@numba.extending.overload(sc.hyp0f1)
def hyp0f1(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('hyp0f1[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.hyp1f1)
def hyp1f1(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('hyp1f1[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.hyp2f1)
def hyp2f1(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('hyp2f1[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.hyperu)
def hyperu(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('hyperu')
        return lambda *args: f(*args)


@numba.extending.overload(sc.i0)
def i0(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('i0')
        return lambda *args: f(*args)


@numba.extending.overload(sc.i0e)
def i0e(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('i0e')
        return lambda *args: f(*args)


@numba.extending.overload(sc.i1)
def i1(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('i1')
        return lambda *args: f(*args)


@numba.extending.overload(sc.i1e)
def i1e(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('i1e')
        return lambda *args: f(*args)


@numba.extending.overload(sc.inv_boxcox)
def inv_boxcox(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('inv_boxcox')
        return lambda *args: f(*args)


@numba.extending.overload(sc.inv_boxcox1p)
def inv_boxcox1p(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('inv_boxcox1p')
        return lambda *args: f(*args)


@numba.extending.overload(sc.it2struve0)
def it2struve0(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('it2struve0')
        return lambda *args: f(*args)


@numba.extending.overload(sc.itmodstruve0)
def itmodstruve0(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('itmodstruve0')
        return lambda *args: f(*args)


@numba.extending.overload(sc.itstruve0)
def itstruve0(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('itstruve0')
        return lambda *args: f(*args)


@numba.extending.overload(sc.iv)
def iv(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('iv[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ive)
def ive(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('ive[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.j0)
def j0(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('j0')
        return lambda *args: f(*args)


@numba.extending.overload(sc.j1)
def j1(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('j1')
        return lambda *args: f(*args)


@numba.extending.overload(sc.jv)
def jv(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('jv[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.jve)
def jve(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('jve[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.k0)
def k0(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('k0')
        return lambda *args: f(*args)


@numba.extending.overload(sc.k0e)
def k0e(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('k0e')
        return lambda *args: f(*args)


@numba.extending.overload(sc.k1)
def k1(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('k1')
        return lambda *args: f(*args)


@numba.extending.overload(sc.k1e)
def k1e(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('k1e')
        return lambda *args: f(*args)


@numba.extending.overload(sc.kei)
def kei(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('kei')
        return lambda *args: f(*args)


@numba.extending.overload(sc.keip)
def keip(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('keip')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ker)
def ker(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('ker')
        return lambda *args: f(*args)


@numba.extending.overload(sc.kerp)
def kerp(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('kerp')
        return lambda *args: f(*args)


@numba.extending.overload(sc.kl_div)
def kl_div(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('kl_div')
        return lambda *args: f(*args)


@numba.extending.overload(sc.kn)
def kn(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('kn[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('kn[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.kolmogi)
def kolmogi(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('kolmogi')
        return lambda *args: f(*args)


@numba.extending.overload(sc.kolmogorov)
def kolmogorov(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('kolmogorov')
        return lambda *args: f(*args)


@numba.extending.overload(sc.kv)
def kv(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('kv[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.kve)
def kve(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('kve[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.log1p)
def log1p(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('log1p[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.log_ndtr)
def log_ndtr(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('log_ndtr[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.loggamma)
def loggamma(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('loggamma[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.logit)
def logit(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('logit[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.lpmv)
def lpmv(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('lpmv')
        return lambda *args: f(*args)


@numba.extending.overload(sc.mathieu_a)
def mathieu_a(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('mathieu_a')
        return lambda *args: f(*args)


@numba.extending.overload(sc.mathieu_b)
def mathieu_b(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('mathieu_b')
        return lambda *args: f(*args)


@numba.extending.overload(sc.modstruve)
def modstruve(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('modstruve')
        return lambda *args: f(*args)


@numba.extending.overload(sc.nbdtr)
def nbdtr(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('nbdtr[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba_long, numba.types.float64,):
        f = get_scalar_function('nbdtr[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.nbdtrc)
def nbdtrc(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('nbdtrc[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba_long, numba.types.float64,):
        f = get_scalar_function('nbdtrc[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.nbdtri)
def nbdtri(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('nbdtri[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba_long, numba.types.float64,):
        f = get_scalar_function('nbdtri[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.nbdtrik)
def nbdtrik(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('nbdtrik')
        return lambda *args: f(*args)


@numba.extending.overload(sc.nbdtrin)
def nbdtrin(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('nbdtrin')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ncfdtr)
def ncfdtr(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('ncfdtr')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ncfdtri)
def ncfdtri(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('ncfdtri')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ncfdtridfd)
def ncfdtridfd(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('ncfdtridfd')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ncfdtridfn)
def ncfdtridfn(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('ncfdtridfn')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ncfdtrinc)
def ncfdtrinc(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('ncfdtrinc')
        return lambda *args: f(*args)


@numba.extending.overload(sc.nctdtr)
def nctdtr(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('nctdtr')
        return lambda *args: f(*args)


@numba.extending.overload(sc.nctdtridf)
def nctdtridf(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('nctdtridf')
        return lambda *args: f(*args)


@numba.extending.overload(sc.nctdtrinc)
def nctdtrinc(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('nctdtrinc')
        return lambda *args: f(*args)


@numba.extending.overload(sc.nctdtrit)
def nctdtrit(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('nctdtrit')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ndtr)
def ndtr(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('ndtr[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.ndtri)
def ndtri(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('ndtri')
        return lambda *args: f(*args)


@numba.extending.overload(sc.nrdtrimn)
def nrdtrimn(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('nrdtrimn')
        return lambda *args: f(*args)


@numba.extending.overload(sc.nrdtrisd)
def nrdtrisd(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('nrdtrisd')
        return lambda *args: f(*args)


@numba.extending.overload(sc.obl_cv)
def obl_cv(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('obl_cv')
        return lambda *args: f(*args)


@numba.extending.overload(sc.owens_t)
def owens_t(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('owens_t')
        return lambda *args: f(*args)


@numba.extending.overload(sc.pdtr)
def pdtr(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('pdtr[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('pdtr[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.pdtrc)
def pdtrc(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('pdtrc[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('pdtrc[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.pdtri)
def pdtri(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('pdtri[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('pdtri[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.pdtrik)
def pdtrik(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('pdtrik')
        return lambda *args: f(*args)


@numba.extending.overload(sc.poch)
def poch(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('poch')
        return lambda *args: f(*args)


@numba.extending.overload(sc.pro_cv)
def pro_cv(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('pro_cv')
        return lambda *args: f(*args)


@numba.extending.overload(sc.pseudo_huber)
def pseudo_huber(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('pseudo_huber')
        return lambda *args: f(*args)


@numba.extending.overload(sc.psi)
def psi(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('psi[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.radian)
def radian(*args):
    if args == (numba.types.float64, numba.types.float64, numba.types.float64,):
        f = get_scalar_function('radian')
        return lambda *args: f(*args)


@numba.extending.overload(sc.rel_entr)
def rel_entr(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('rel_entr')
        return lambda *args: f(*args)


@numba.extending.overload(sc.rgamma)
def rgamma(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('rgamma[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.round)
def round(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('round')
        return lambda *args: f(*args)


@numba.extending.overload(sc.sindg)
def sindg(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('sindg')
        return lambda *args: f(*args)


@numba.extending.overload(sc.smirnov)
def smirnov(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('smirnov[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('smirnov[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.smirnovi)
def smirnovi(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('smirnovi[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('smirnovi[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.spence)
def spence(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('spence[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.stdtr)
def stdtr(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('stdtr')
        return lambda *args: f(*args)


@numba.extending.overload(sc.stdtridf)
def stdtridf(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('stdtridf')
        return lambda *args: f(*args)


@numba.extending.overload(sc.stdtrit)
def stdtrit(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('stdtrit')
        return lambda *args: f(*args)


@numba.extending.overload(sc.struve)
def struve(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('struve')
        return lambda *args: f(*args)


@numba.extending.overload(sc.tandg)
def tandg(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('tandg')
        return lambda *args: f(*args)


@numba.extending.overload(sc.tklmbda)
def tklmbda(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('tklmbda')
        return lambda *args: f(*args)


@numba.extending.overload(sc.xlog1py)
def xlog1py(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('xlog1py[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.xlogy)
def xlogy(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('xlogy[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.y0)
def y0(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('y0')
        return lambda *args: f(*args)


@numba.extending.overload(sc.y1)
def y1(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('y1')
        return lambda *args: f(*args)


@numba.extending.overload(sc.yn)
def yn(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('yn[double]')
        return lambda *args: f(*args)

    if args == (numba_long, numba.types.float64,):
        f = get_scalar_function('yn[long]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.yv)
def yv(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('yv[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.yve)
def yve(*args):
    if args == (numba.types.float64, numba.types.float64,):
        f = get_scalar_function('yve[double]')
        return lambda *args: f(*args)


@numba.extending.overload(sc.zetac)
def zetac(*args):
    if args == (numba.types.float64,):
        f = get_scalar_function('zetac')
        return lambda *args: f(*args)

