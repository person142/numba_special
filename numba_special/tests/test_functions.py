import numba
import scipy.special as sc
import numba_special


def test_gamma():
    @numba.njit
    def gamma_wrapper(x):
        return sc.gamma(x)

    assert gamma_wrapper(5.0) == sc.gamma(5.0)
