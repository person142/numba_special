
#cython: language_level=3
from cpython.long cimport PyLong_FromVoidPtr

cimport scipy.special.cython_special as sc


functions = {
    'agm': PyLong_FromVoidPtr(<void *>sc.agm),
    'bdtr[double]': PyLong_FromVoidPtr(<void *>sc.bdtr[double]),
    'bdtr[long]': PyLong_FromVoidPtr(<void *>sc.bdtr[long]),
    'bdtrc[double]': PyLong_FromVoidPtr(<void *>sc.bdtrc[double]),
    'bdtrc[long]': PyLong_FromVoidPtr(<void *>sc.bdtrc[long]),
    'bdtri[double]': PyLong_FromVoidPtr(<void *>sc.bdtri[double]),
    'bdtri[long]': PyLong_FromVoidPtr(<void *>sc.bdtri[long]),
    'bdtrik': PyLong_FromVoidPtr(<void *>sc.bdtrik),
    'bdtrin': PyLong_FromVoidPtr(<void *>sc.bdtrin),
    'bei': PyLong_FromVoidPtr(<void *>sc.bei),
    'beip': PyLong_FromVoidPtr(<void *>sc.beip),
    'ber': PyLong_FromVoidPtr(<void *>sc.ber),
    'berp': PyLong_FromVoidPtr(<void *>sc.berp),
    'besselpoly': PyLong_FromVoidPtr(<void *>sc.besselpoly),
    'beta': PyLong_FromVoidPtr(<void *>sc.beta),
    'betainc': PyLong_FromVoidPtr(<void *>sc.betainc),
    'betaincinv': PyLong_FromVoidPtr(<void *>sc.betaincinv),
    'betaln': PyLong_FromVoidPtr(<void *>sc.betaln),
    'binom': PyLong_FromVoidPtr(<void *>sc.binom),
    'boxcox': PyLong_FromVoidPtr(<void *>sc.boxcox),
    'boxcox1p': PyLong_FromVoidPtr(<void *>sc.boxcox1p),
    'btdtr': PyLong_FromVoidPtr(<void *>sc.btdtr),
    'btdtri': PyLong_FromVoidPtr(<void *>sc.btdtri),
    'btdtria': PyLong_FromVoidPtr(<void *>sc.btdtria),
    'btdtrib': PyLong_FromVoidPtr(<void *>sc.btdtrib),
    'cbrt': PyLong_FromVoidPtr(<void *>sc.cbrt),
    'chdtr': PyLong_FromVoidPtr(<void *>sc.chdtr),
    'chdtrc': PyLong_FromVoidPtr(<void *>sc.chdtrc),
    'chdtri': PyLong_FromVoidPtr(<void *>sc.chdtri),
    'chdtriv': PyLong_FromVoidPtr(<void *>sc.chdtriv),
    'chndtr': PyLong_FromVoidPtr(<void *>sc.chndtr),
    'chndtridf': PyLong_FromVoidPtr(<void *>sc.chndtridf),
    'chndtrinc': PyLong_FromVoidPtr(<void *>sc.chndtrinc),
    'chndtrix': PyLong_FromVoidPtr(<void *>sc.chndtrix),
    'cosdg': PyLong_FromVoidPtr(<void *>sc.cosdg),
    'cosm1': PyLong_FromVoidPtr(<void *>sc.cosm1),
    'cotdg': PyLong_FromVoidPtr(<void *>sc.cotdg),
    'dawsn[double]': PyLong_FromVoidPtr(<void *>sc.dawsn[double]),
    'ellipe': PyLong_FromVoidPtr(<void *>sc.ellipe),
    'ellipeinc': PyLong_FromVoidPtr(<void *>sc.ellipeinc),
    'ellipkinc': PyLong_FromVoidPtr(<void *>sc.ellipkinc),
    'ellipkm1': PyLong_FromVoidPtr(<void *>sc.ellipkm1),
    'entr': PyLong_FromVoidPtr(<void *>sc.entr),
    'erf[double]': PyLong_FromVoidPtr(<void *>sc.erf[double]),
    'erfc[double]': PyLong_FromVoidPtr(<void *>sc.erfc[double]),
    'erfcx[double]': PyLong_FromVoidPtr(<void *>sc.erfcx[double]),
    'erfi[double]': PyLong_FromVoidPtr(<void *>sc.erfi[double]),
    'eval_chebyc[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_chebyc[double, double]),
    'eval_chebyc[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_chebyc[long, double]),
    'eval_chebys[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_chebys[double, double]),
    'eval_chebys[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_chebys[long, double]),
    'eval_chebyt[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_chebyt[double, double]),
    'eval_chebyt[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_chebyt[long, double]),
    'eval_chebyu[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_chebyu[double, double]),
    'eval_chebyu[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_chebyu[long, double]),
    'eval_gegenbauer[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_gegenbauer[double, double]),
    'eval_gegenbauer[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_gegenbauer[long, double]),
    'eval_genlaguerre[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_genlaguerre[double, double]),
    'eval_genlaguerre[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_genlaguerre[long, double]),
    'eval_hermite': PyLong_FromVoidPtr(<void *>sc.eval_hermite),
    'eval_hermitenorm': PyLong_FromVoidPtr(<void *>sc.eval_hermitenorm),
    'eval_jacobi[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_jacobi[double, double]),
    'eval_jacobi[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_jacobi[long, double]),
    'eval_laguerre[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_laguerre[double, double]),
    'eval_laguerre[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_laguerre[long, double]),
    'eval_legendre[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_legendre[double, double]),
    'eval_legendre[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_legendre[long, double]),
    'eval_sh_chebyt[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_sh_chebyt[double, double]),
    'eval_sh_chebyt[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_sh_chebyt[long, double]),
    'eval_sh_chebyu[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_sh_chebyu[double, double]),
    'eval_sh_chebyu[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_sh_chebyu[long, double]),
    'eval_sh_jacobi[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_sh_jacobi[double, double]),
    'eval_sh_jacobi[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_sh_jacobi[long, double]),
    'eval_sh_legendre[double, double]': PyLong_FromVoidPtr(<void *>sc.eval_sh_legendre[double, double]),
    'eval_sh_legendre[long, double]': PyLong_FromVoidPtr(<void *>sc.eval_sh_legendre[long, double]),
    'exp1[double]': PyLong_FromVoidPtr(<void *>sc.exp1[double]),
    'exp10': PyLong_FromVoidPtr(<void *>sc.exp10),
    'exp2': PyLong_FromVoidPtr(<void *>sc.exp2),
    'expi[double]': PyLong_FromVoidPtr(<void *>sc.expi[double]),
    'expit[double]': PyLong_FromVoidPtr(<void *>sc.expit[double]),
    'expit[float]': PyLong_FromVoidPtr(<void *>sc.expit[float]),
    'expm1[double]': PyLong_FromVoidPtr(<void *>sc.expm1[double]),
    'expn[double]': PyLong_FromVoidPtr(<void *>sc.expn[double]),
    'expn[long]': PyLong_FromVoidPtr(<void *>sc.expn[long]),
    'exprel': PyLong_FromVoidPtr(<void *>sc.exprel),
    'fdtr': PyLong_FromVoidPtr(<void *>sc.fdtr),
    'fdtrc': PyLong_FromVoidPtr(<void *>sc.fdtrc),
    'fdtri': PyLong_FromVoidPtr(<void *>sc.fdtri),
    'fdtridfd': PyLong_FromVoidPtr(<void *>sc.fdtridfd),
    'gamma[double]': PyLong_FromVoidPtr(<void *>sc.gamma[double]),
    'gammainc': PyLong_FromVoidPtr(<void *>sc.gammainc),
    'gammaincc': PyLong_FromVoidPtr(<void *>sc.gammaincc),
    'gammainccinv': PyLong_FromVoidPtr(<void *>sc.gammainccinv),
    'gammaincinv': PyLong_FromVoidPtr(<void *>sc.gammaincinv),
    'gammaln': PyLong_FromVoidPtr(<void *>sc.gammaln),
    'gammasgn': PyLong_FromVoidPtr(<void *>sc.gammasgn),
    'gdtr': PyLong_FromVoidPtr(<void *>sc.gdtr),
    'gdtrc': PyLong_FromVoidPtr(<void *>sc.gdtrc),
    'gdtria': PyLong_FromVoidPtr(<void *>sc.gdtria),
    'gdtrib': PyLong_FromVoidPtr(<void *>sc.gdtrib),
    'gdtrix': PyLong_FromVoidPtr(<void *>sc.gdtrix),
    'huber': PyLong_FromVoidPtr(<void *>sc.huber),
    'hyp0f1[double]': PyLong_FromVoidPtr(<void *>sc.hyp0f1[double]),
    'hyp1f1[double]': PyLong_FromVoidPtr(<void *>sc.hyp1f1[double]),
    'hyp2f1[double]': PyLong_FromVoidPtr(<void *>sc.hyp2f1[double]),
    'hyperu': PyLong_FromVoidPtr(<void *>sc.hyperu),
    'i0': PyLong_FromVoidPtr(<void *>sc.i0),
    'i0e': PyLong_FromVoidPtr(<void *>sc.i0e),
    'i1': PyLong_FromVoidPtr(<void *>sc.i1),
    'i1e': PyLong_FromVoidPtr(<void *>sc.i1e),
    'inv_boxcox': PyLong_FromVoidPtr(<void *>sc.inv_boxcox),
    'inv_boxcox1p': PyLong_FromVoidPtr(<void *>sc.inv_boxcox1p),
    'it2struve0': PyLong_FromVoidPtr(<void *>sc.it2struve0),
    'itmodstruve0': PyLong_FromVoidPtr(<void *>sc.itmodstruve0),
    'itstruve0': PyLong_FromVoidPtr(<void *>sc.itstruve0),
    'iv[double]': PyLong_FromVoidPtr(<void *>sc.iv[double]),
    'ive[double]': PyLong_FromVoidPtr(<void *>sc.ive[double]),
    'j0': PyLong_FromVoidPtr(<void *>sc.j0),
    'j1': PyLong_FromVoidPtr(<void *>sc.j1),
    'jv[double]': PyLong_FromVoidPtr(<void *>sc.jv[double]),
    'jve[double]': PyLong_FromVoidPtr(<void *>sc.jve[double]),
    'k0': PyLong_FromVoidPtr(<void *>sc.k0),
    'k0e': PyLong_FromVoidPtr(<void *>sc.k0e),
    'k1': PyLong_FromVoidPtr(<void *>sc.k1),
    'k1e': PyLong_FromVoidPtr(<void *>sc.k1e),
    'kei': PyLong_FromVoidPtr(<void *>sc.kei),
    'keip': PyLong_FromVoidPtr(<void *>sc.keip),
    'ker': PyLong_FromVoidPtr(<void *>sc.ker),
    'kerp': PyLong_FromVoidPtr(<void *>sc.kerp),
    'kl_div': PyLong_FromVoidPtr(<void *>sc.kl_div),
    'kn[double]': PyLong_FromVoidPtr(<void *>sc.kn[double]),
    'kn[long]': PyLong_FromVoidPtr(<void *>sc.kn[long]),
    'kolmogi': PyLong_FromVoidPtr(<void *>sc.kolmogi),
    'kolmogorov': PyLong_FromVoidPtr(<void *>sc.kolmogorov),
    'kv[double]': PyLong_FromVoidPtr(<void *>sc.kv[double]),
    'kve[double]': PyLong_FromVoidPtr(<void *>sc.kve[double]),
    'log1p[double]': PyLong_FromVoidPtr(<void *>sc.log1p[double]),
    'log_ndtr[double]': PyLong_FromVoidPtr(<void *>sc.log_ndtr[double]),
    'loggamma[double]': PyLong_FromVoidPtr(<void *>sc.loggamma[double]),
    'logit[double]': PyLong_FromVoidPtr(<void *>sc.logit[double]),
    'logit[float]': PyLong_FromVoidPtr(<void *>sc.logit[float]),
    'lpmv': PyLong_FromVoidPtr(<void *>sc.lpmv),
    'mathieu_a': PyLong_FromVoidPtr(<void *>sc.mathieu_a),
    'mathieu_b': PyLong_FromVoidPtr(<void *>sc.mathieu_b),
    'modstruve': PyLong_FromVoidPtr(<void *>sc.modstruve),
    'nbdtr[double]': PyLong_FromVoidPtr(<void *>sc.nbdtr[double]),
    'nbdtr[long]': PyLong_FromVoidPtr(<void *>sc.nbdtr[long]),
    'nbdtrc[double]': PyLong_FromVoidPtr(<void *>sc.nbdtrc[double]),
    'nbdtrc[long]': PyLong_FromVoidPtr(<void *>sc.nbdtrc[long]),
    'nbdtri[double]': PyLong_FromVoidPtr(<void *>sc.nbdtri[double]),
    'nbdtri[long]': PyLong_FromVoidPtr(<void *>sc.nbdtri[long]),
    'nbdtrik': PyLong_FromVoidPtr(<void *>sc.nbdtrik),
    'nbdtrin': PyLong_FromVoidPtr(<void *>sc.nbdtrin),
    'ncfdtr': PyLong_FromVoidPtr(<void *>sc.ncfdtr),
    'ncfdtri': PyLong_FromVoidPtr(<void *>sc.ncfdtri),
    'ncfdtridfd': PyLong_FromVoidPtr(<void *>sc.ncfdtridfd),
    'ncfdtridfn': PyLong_FromVoidPtr(<void *>sc.ncfdtridfn),
    'ncfdtrinc': PyLong_FromVoidPtr(<void *>sc.ncfdtrinc),
    'nctdtr': PyLong_FromVoidPtr(<void *>sc.nctdtr),
    'nctdtridf': PyLong_FromVoidPtr(<void *>sc.nctdtridf),
    'nctdtrinc': PyLong_FromVoidPtr(<void *>sc.nctdtrinc),
    'nctdtrit': PyLong_FromVoidPtr(<void *>sc.nctdtrit),
    'ndtr[double]': PyLong_FromVoidPtr(<void *>sc.ndtr[double]),
    'ndtri': PyLong_FromVoidPtr(<void *>sc.ndtri),
    'nrdtrimn': PyLong_FromVoidPtr(<void *>sc.nrdtrimn),
    'nrdtrisd': PyLong_FromVoidPtr(<void *>sc.nrdtrisd),
    'obl_cv': PyLong_FromVoidPtr(<void *>sc.obl_cv),
    'owens_t': PyLong_FromVoidPtr(<void *>sc.owens_t),
    'pdtr[double]': PyLong_FromVoidPtr(<void *>sc.pdtr[double]),
    'pdtr[long]': PyLong_FromVoidPtr(<void *>sc.pdtr[long]),
    'pdtrc[double]': PyLong_FromVoidPtr(<void *>sc.pdtrc[double]),
    'pdtrc[long]': PyLong_FromVoidPtr(<void *>sc.pdtrc[long]),
    'pdtri[double]': PyLong_FromVoidPtr(<void *>sc.pdtri[double]),
    'pdtri[long]': PyLong_FromVoidPtr(<void *>sc.pdtri[long]),
    'pdtrik': PyLong_FromVoidPtr(<void *>sc.pdtrik),
    'poch': PyLong_FromVoidPtr(<void *>sc.poch),
    'pro_cv': PyLong_FromVoidPtr(<void *>sc.pro_cv),
    'pseudo_huber': PyLong_FromVoidPtr(<void *>sc.pseudo_huber),
    'psi[double]': PyLong_FromVoidPtr(<void *>sc.psi[double]),
    'radian': PyLong_FromVoidPtr(<void *>sc.radian),
    'rel_entr': PyLong_FromVoidPtr(<void *>sc.rel_entr),
    'rgamma[double]': PyLong_FromVoidPtr(<void *>sc.rgamma[double]),
    'round': PyLong_FromVoidPtr(<void *>sc.round),
    'sindg': PyLong_FromVoidPtr(<void *>sc.sindg),
    'smirnov[double]': PyLong_FromVoidPtr(<void *>sc.smirnov[double]),
    'smirnov[long]': PyLong_FromVoidPtr(<void *>sc.smirnov[long]),
    'smirnovi[double]': PyLong_FromVoidPtr(<void *>sc.smirnovi[double]),
    'smirnovi[long]': PyLong_FromVoidPtr(<void *>sc.smirnovi[long]),
    'spence[double]': PyLong_FromVoidPtr(<void *>sc.spence[double]),
    'stdtr': PyLong_FromVoidPtr(<void *>sc.stdtr),
    'stdtridf': PyLong_FromVoidPtr(<void *>sc.stdtridf),
    'stdtrit': PyLong_FromVoidPtr(<void *>sc.stdtrit),
    'struve': PyLong_FromVoidPtr(<void *>sc.struve),
    'tandg': PyLong_FromVoidPtr(<void *>sc.tandg),
    'tklmbda': PyLong_FromVoidPtr(<void *>sc.tklmbda),
    'xlog1py[double]': PyLong_FromVoidPtr(<void *>sc.xlog1py[double]),
    'xlogy[double]': PyLong_FromVoidPtr(<void *>sc.xlogy[double]),
    'y0': PyLong_FromVoidPtr(<void *>sc.y0),
    'y1': PyLong_FromVoidPtr(<void *>sc.y1),
    'yn[double]': PyLong_FromVoidPtr(<void *>sc.yn[double]),
    'yn[long]': PyLong_FromVoidPtr(<void *>sc.yn[long]),
    'yv[double]': PyLong_FromVoidPtr(<void *>sc.yv[double]),
    'yve[double]': PyLong_FromVoidPtr(<void *>sc.yve[double]),
    'zetac': PyLong_FromVoidPtr(<void *>sc.zetac)
}
