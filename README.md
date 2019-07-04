# Numba Special

Numba special allows SciPy's special functions to be used in
Numba.

```python
>>> import scipy.special as sc
>>> import numba_special
>>> import numba
>>> @numba.njit
... def gamma_plus_1(x):
...     return sc.gamma(x) + 1.0
...
>>> gamma_plus_1(5.0)
25.0
```
