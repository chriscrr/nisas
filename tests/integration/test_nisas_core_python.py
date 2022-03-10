import pytest
from nisas.core import main
import numpy as np
from . import test_nisas_core as tnc

def test_nisas_runs():
    np.testing.assert_array_equal(main(), np.ones(5))

def test_nisas_runs_wrapped_cython():
    tnc.test_nisas_runs_using_cython()
