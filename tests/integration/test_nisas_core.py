import pytest
from nisas.core import main
import numpy as np
import functools
import inspect

def cytest(func):
    """
    Wraps `func` in a plain Python function.
    """

    @functools.wraps(func)
    def wrapped(*args, **kwargs):
        bound = inspect.signature(func).bind(*args, **kwargs)
        return func(*bound.args, **bound.kwargs)

    return wrapped


@cytest
def test_nisas_runs_using_cython():
    np.testing.assert_array_equal(main(), np.ones(5))
