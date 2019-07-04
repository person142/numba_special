import numba
import scipy.special as sc
import numba_special


def test_erf():
    @numba.njit
    def erf_wrapper(x):
        return sc.erf(x)

    assert erf_wrapper(2.0) == sc.erf(2.0)


def test_gamma():
    @numba.njit
    def gamma_wrapper(x):
        return sc.gamma(x)

    assert gamma_wrapper(5.0) == sc.gamma(5.0)
