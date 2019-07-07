Numba Special
=============

Numba special allows SciPy's special functions to be used in
Numba::

  >>> import numba
  >>> import scipy.special as sc
  >>> import numba_special  # The import generates Numba overloads for special
  >>> @numba.njit
  ... def gamma_plus_1(x):
  ...     return sc.gamma(x) + 1.0
  ...
  >>> gamma_plus_1(5.0)
  25.0

The complete list of overloaded functions can be found here:

.. toctree::
   :maxdepth: 1

   numba_special
