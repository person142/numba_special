# Numba Special

[![CircleCI](https://circleci.com/gh/person142/numba_special/tree/master.svg?style=svg)](https://circleci.com/gh/person142/numba_special/tree/master)

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
