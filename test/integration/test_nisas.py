import pytest
from nisas.core import main
import numpy as np

def test_nisas_runs():
    np.testing.assert_array_equal(main(), np.ones(5))
