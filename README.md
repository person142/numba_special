# Numba Special

[![CircleCI](https://circleci.com/gh/person142/numba_special/tree/master.svg?style=svg)](https://circleci.com/gh/person142/numba_special/tree/master) [![Documentation Status](https://readthedocs.org/projects/numba-special/badge/?version=latest)](https://numba-special.readthedocs.io/en/latest/?badge=latest)

Numba special allows SciPy's special functions to be used in
Numba.

```python
>>> import numba
>>> import scipy.special as sc
>>> import numba_special  # The import generates Numba overloads for special
>>> @numba.njit
... def gamma_plus_1(x):
...     return sc.gamma(x) + 1.0
...
>>> gamma_plus_1(5.0)
25.0
```

For detailed information on which functions can be used from Numba,
check the
[documentation](https://numba-special.readthedocs.io/en/latest/).
