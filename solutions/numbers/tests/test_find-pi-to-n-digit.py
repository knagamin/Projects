import pytest
from solutions.numbers import find_pi

# 3.141592653589793
def test_find_pi():
    assert find_pi.find_pi_n_digits(1) == 1
