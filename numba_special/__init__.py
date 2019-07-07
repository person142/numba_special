"""
Available overloads
===================

The following variants of SciPy's special functions can be used inside
Numba jitted code.

- :data:`scipy.special.agm`::

    float64 agm(float64, float64)

- :data:`scipy.special.bdtr`::

    float64 bdtr(float64, float64, float64)

- :data:`scipy.special.bdtrc`::

    float64 bdtrc(float64, float64, float64)

- :data:`scipy.special.bdtri`::

    float64 bdtri(float64, float64, float64)

- :data:`scipy.special.bdtrik`::

    float64 bdtrik(float64, float64, float64)

- :data:`scipy.special.bdtrin`::

    float64 bdtrin(float64, float64, float64)

- :data:`scipy.special.bei`::

    float64 bei(float64)

- :data:`scipy.special.beip`::

    float64 beip(float64)

- :data:`scipy.special.ber`::

    float64 ber(float64)

- :data:`scipy.special.berp`::

    float64 berp(float64)

- :data:`scipy.special.besselpoly`::

    float64 besselpoly(float64, float64, float64)

- :data:`scipy.special.beta`::

    float64 beta(float64, float64)

- :data:`scipy.special.betainc`::

    float64 betainc(float64, float64, float64)

- :data:`scipy.special.betaincinv`::

    float64 betaincinv(float64, float64, float64)

- :data:`scipy.special.betaln`::

    float64 betaln(float64, float64)

- :data:`scipy.special.binom`::

    float64 binom(float64, float64)

- :data:`scipy.special.boxcox`::

    float64 boxcox(float64, float64)

- :data:`scipy.special.boxcox1p`::

    float64 boxcox1p(float64, float64)

- :data:`scipy.special.btdtr`::

    float64 btdtr(float64, float64, float64)

- :data:`scipy.special.btdtri`::

    float64 btdtri(float64, float64, float64)

- :data:`scipy.special.btdtria`::

    float64 btdtria(float64, float64, float64)

- :data:`scipy.special.btdtrib`::

    float64 btdtrib(float64, float64, float64)

- :data:`scipy.special.cbrt`::

    float64 cbrt(float64)

- :data:`scipy.special.chdtr`::

    float64 chdtr(float64, float64)

- :data:`scipy.special.chdtrc`::

    float64 chdtrc(float64, float64)

- :data:`scipy.special.chdtri`::

    float64 chdtri(float64, float64)

- :data:`scipy.special.chdtriv`::

    float64 chdtriv(float64, float64)

- :data:`scipy.special.chndtr`::

    float64 chndtr(float64, float64, float64)

- :data:`scipy.special.chndtridf`::

    float64 chndtridf(float64, float64, float64)

- :data:`scipy.special.chndtrinc`::

    float64 chndtrinc(float64, float64, float64)

- :data:`scipy.special.chndtrix`::

    float64 chndtrix(float64, float64, float64)

- :data:`scipy.special.cosdg`::

    float64 cosdg(float64)

- :data:`scipy.special.cosm1`::

    float64 cosm1(float64)

- :data:`scipy.special.cotdg`::

    float64 cotdg(float64)

- :data:`scipy.special.dawsn`::

    float64 dawsn(float64)

- :data:`scipy.special.ellipe`::

    float64 ellipe(float64)

- :data:`scipy.special.ellipeinc`::

    float64 ellipeinc(float64, float64)

- :data:`scipy.special.ellipkinc`::

    float64 ellipkinc(float64, float64)

- :data:`scipy.special.ellipkm1`::

    float64 ellipkm1(float64)

- :data:`scipy.special.entr`::

    float64 entr(float64)

- :data:`scipy.special.erf`::

    float64 erf(float64)

- :data:`scipy.special.erfc`::

    float64 erfc(float64)

- :data:`scipy.special.erfcx`::

    float64 erfcx(float64)

- :data:`scipy.special.erfi`::

    float64 erfi(float64)

- :data:`scipy.special.eval_chebyc`::

    float64 eval_chebyc(float64, float64)

- :data:`scipy.special.eval_chebys`::

    float64 eval_chebys(float64, float64)

- :data:`scipy.special.eval_chebyt`::

    float64 eval_chebyt(float64, float64)

- :data:`scipy.special.eval_chebyu`::

    float64 eval_chebyu(float64, float64)

- :data:`scipy.special.eval_gegenbauer`::

    float64 eval_gegenbauer(float64, float64, float64)

- :data:`scipy.special.eval_genlaguerre`::

    float64 eval_genlaguerre(float64, float64, float64)

- :data:`scipy.special.eval_jacobi`::

    float64 eval_jacobi(float64, float64, float64, float64)

- :data:`scipy.special.eval_laguerre`::

    float64 eval_laguerre(float64, float64)

- :data:`scipy.special.eval_legendre`::

    float64 eval_legendre(float64, float64)

- :data:`scipy.special.eval_sh_chebyt`::

    float64 eval_sh_chebyt(float64, float64)

- :data:`scipy.special.eval_sh_chebyu`::

    float64 eval_sh_chebyu(float64, float64)

- :data:`scipy.special.eval_sh_jacobi`::

    float64 eval_sh_jacobi(float64, float64, float64, float64)

- :data:`scipy.special.eval_sh_legendre`::

    float64 eval_sh_legendre(float64, float64)

- :data:`scipy.special.exp1`::

    float64 exp1(float64)

- :data:`scipy.special.exp10`::

    float64 exp10(float64)

- :data:`scipy.special.exp2`::

    float64 exp2(float64)

- :data:`scipy.special.expi`::

    float64 expi(float64)

- :data:`scipy.special.expit`::

    float64 expit(float64)

- :data:`scipy.special.expm1`::

    float64 expm1(float64)

- :data:`scipy.special.expn`::

    float64 expn(float64, float64)

- :data:`scipy.special.exprel`::

    float64 exprel(float64)

- :data:`scipy.special.fdtr`::

    float64 fdtr(float64, float64, float64)

- :data:`scipy.special.fdtrc`::

    float64 fdtrc(float64, float64, float64)

- :data:`scipy.special.fdtri`::

    float64 fdtri(float64, float64, float64)

- :data:`scipy.special.fdtridfd`::

    float64 fdtridfd(float64, float64, float64)

- :data:`scipy.special.gamma`::

    float64 gamma(float64)

- :data:`scipy.special.gammainc`::

    float64 gammainc(float64, float64)

- :data:`scipy.special.gammaincc`::

    float64 gammaincc(float64, float64)

- :data:`scipy.special.gammainccinv`::

    float64 gammainccinv(float64, float64)

- :data:`scipy.special.gammaincinv`::

    float64 gammaincinv(float64, float64)

- :data:`scipy.special.gammaln`::

    float64 gammaln(float64)

- :data:`scipy.special.gammasgn`::

    float64 gammasgn(float64)

- :data:`scipy.special.gdtr`::

    float64 gdtr(float64, float64, float64)

- :data:`scipy.special.gdtrc`::

    float64 gdtrc(float64, float64, float64)

- :data:`scipy.special.gdtria`::

    float64 gdtria(float64, float64, float64)

- :data:`scipy.special.gdtrib`::

    float64 gdtrib(float64, float64, float64)

- :data:`scipy.special.gdtrix`::

    float64 gdtrix(float64, float64, float64)

- :data:`scipy.special.huber`::

    float64 huber(float64, float64)

- :data:`scipy.special.hyp0f1`::

    float64 hyp0f1(float64, float64)

- :data:`scipy.special.hyp1f1`::

    float64 hyp1f1(float64, float64, float64)

- :data:`scipy.special.hyp2f1`::

    float64 hyp2f1(float64, float64, float64, float64)

- :data:`scipy.special.hyperu`::

    float64 hyperu(float64, float64, float64)

- :data:`scipy.special.i0`::

    float64 i0(float64)

- :data:`scipy.special.i0e`::

    float64 i0e(float64)

- :data:`scipy.special.i1`::

    float64 i1(float64)

- :data:`scipy.special.i1e`::

    float64 i1e(float64)

- :data:`scipy.special.inv_boxcox`::

    float64 inv_boxcox(float64, float64)

- :data:`scipy.special.inv_boxcox1p`::

    float64 inv_boxcox1p(float64, float64)

- :data:`scipy.special.it2struve0`::

    float64 it2struve0(float64)

- :data:`scipy.special.itmodstruve0`::

    float64 itmodstruve0(float64)

- :data:`scipy.special.itstruve0`::

    float64 itstruve0(float64)

- :data:`scipy.special.iv`::

    float64 iv(float64, float64)

- :data:`scipy.special.ive`::

    float64 ive(float64, float64)

- :data:`scipy.special.j0`::

    float64 j0(float64)

- :data:`scipy.special.j1`::

    float64 j1(float64)

- :data:`scipy.special.jv`::

    float64 jv(float64, float64)

- :data:`scipy.special.jve`::

    float64 jve(float64, float64)

- :data:`scipy.special.k0`::

    float64 k0(float64)

- :data:`scipy.special.k0e`::

    float64 k0e(float64)

- :data:`scipy.special.k1`::

    float64 k1(float64)

- :data:`scipy.special.k1e`::

    float64 k1e(float64)

- :data:`scipy.special.kei`::

    float64 kei(float64)

- :data:`scipy.special.keip`::

    float64 keip(float64)

- :data:`scipy.special.ker`::

    float64 ker(float64)

- :data:`scipy.special.kerp`::

    float64 kerp(float64)

- :data:`scipy.special.kl_div`::

    float64 kl_div(float64, float64)

- :data:`scipy.special.kn`::

    float64 kn(float64, float64)

- :data:`scipy.special.kolmogi`::

    float64 kolmogi(float64)

- :data:`scipy.special.kolmogorov`::

    float64 kolmogorov(float64)

- :data:`scipy.special.kv`::

    float64 kv(float64, float64)

- :data:`scipy.special.kve`::

    float64 kve(float64, float64)

- :data:`scipy.special.log1p`::

    float64 log1p(float64)

- :data:`scipy.special.log_ndtr`::

    float64 log_ndtr(float64)

- :data:`scipy.special.loggamma`::

    float64 loggamma(float64)

- :data:`scipy.special.logit`::

    float64 logit(float64)

- :data:`scipy.special.lpmv`::

    float64 lpmv(float64, float64, float64)

- :data:`scipy.special.mathieu_a`::

    float64 mathieu_a(float64, float64)

- :data:`scipy.special.mathieu_b`::

    float64 mathieu_b(float64, float64)

- :data:`scipy.special.modstruve`::

    float64 modstruve(float64, float64)

- :data:`scipy.special.nbdtr`::

    float64 nbdtr(float64, float64, float64)

- :data:`scipy.special.nbdtrc`::

    float64 nbdtrc(float64, float64, float64)

- :data:`scipy.special.nbdtri`::

    float64 nbdtri(float64, float64, float64)

- :data:`scipy.special.nbdtrik`::

    float64 nbdtrik(float64, float64, float64)

- :data:`scipy.special.nbdtrin`::

    float64 nbdtrin(float64, float64, float64)

- :data:`scipy.special.ncfdtr`::

    float64 ncfdtr(float64, float64, float64, float64)

- :data:`scipy.special.ncfdtri`::

    float64 ncfdtri(float64, float64, float64, float64)

- :data:`scipy.special.ncfdtridfd`::

    float64 ncfdtridfd(float64, float64, float64, float64)

- :data:`scipy.special.ncfdtridfn`::

    float64 ncfdtridfn(float64, float64, float64, float64)

- :data:`scipy.special.ncfdtrinc`::

    float64 ncfdtrinc(float64, float64, float64, float64)

- :data:`scipy.special.nctdtr`::

    float64 nctdtr(float64, float64, float64)

- :data:`scipy.special.nctdtridf`::

    float64 nctdtridf(float64, float64, float64)

- :data:`scipy.special.nctdtrinc`::

    float64 nctdtrinc(float64, float64, float64)

- :data:`scipy.special.nctdtrit`::

    float64 nctdtrit(float64, float64, float64)

- :data:`scipy.special.ndtr`::

    float64 ndtr(float64)

- :data:`scipy.special.ndtri`::

    float64 ndtri(float64)

- :data:`scipy.special.nrdtrimn`::

    float64 nrdtrimn(float64, float64, float64)

- :data:`scipy.special.nrdtrisd`::

    float64 nrdtrisd(float64, float64, float64)

- :data:`scipy.special.obl_cv`::

    float64 obl_cv(float64, float64, float64)

- :data:`scipy.special.owens_t`::

    float64 owens_t(float64, float64)

- :data:`scipy.special.pdtr`::

    float64 pdtr(float64, float64)

- :data:`scipy.special.pdtrc`::

    float64 pdtrc(float64, float64)

- :data:`scipy.special.pdtri`::

    float64 pdtri(float64, float64)

- :data:`scipy.special.pdtrik`::

    float64 pdtrik(float64, float64)

- :data:`scipy.special.poch`::

    float64 poch(float64, float64)

- :data:`scipy.special.pro_cv`::

    float64 pro_cv(float64, float64, float64)

- :data:`scipy.special.pseudo_huber`::

    float64 pseudo_huber(float64, float64)

- :data:`scipy.special.psi`::

    float64 psi(float64)

- :data:`scipy.special.radian`::

    float64 radian(float64, float64, float64)

- :data:`scipy.special.rel_entr`::

    float64 rel_entr(float64, float64)

- :data:`scipy.special.rgamma`::

    float64 rgamma(float64)

- :data:`scipy.special.round`::

    float64 round(float64)

- :data:`scipy.special.sindg`::

    float64 sindg(float64)

- :data:`scipy.special.smirnov`::

    float64 smirnov(float64, float64)

- :data:`scipy.special.smirnovi`::

    float64 smirnovi(float64, float64)

- :data:`scipy.special.spence`::

    float64 spence(float64)

- :data:`scipy.special.stdtr`::

    float64 stdtr(float64, float64)

- :data:`scipy.special.stdtridf`::

    float64 stdtridf(float64, float64)

- :data:`scipy.special.stdtrit`::

    float64 stdtrit(float64, float64)

- :data:`scipy.special.struve`::

    float64 struve(float64, float64)

- :data:`scipy.special.tandg`::

    float64 tandg(float64)

- :data:`scipy.special.tklmbda`::

    float64 tklmbda(float64, float64)

- :data:`scipy.special.xlog1py`::

    float64 xlog1py(float64, float64)

- :data:`scipy.special.xlogy`::

    float64 xlogy(float64, float64)

- :data:`scipy.special.y0`::

    float64 y0(float64)

- :data:`scipy.special.y1`::

    float64 y1(float64)

- :data:`scipy.special.yn`::

    float64 yn(float64, float64)

- :data:`scipy.special.yv`::

    float64 yv(float64, float64)

- :data:`scipy.special.yve`::

    float64 yve(float64, float64)

- :data:`scipy.special.zetac`::

    float64 zetac(float64)
"""
from . import numba_overloads
