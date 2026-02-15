import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(3, 5) == 8

def test_add_negative_numbers():
    assert add(-2, -7) == -9

def test_add_zero():
    assert add(0, 0) == 0

def test_add_positive_and_negative():
    assert add(10, -3) == 7

def test_add_float_numbers():
    assert add(2.5, 4.1) == pytest.approx(6.6)

def test_add_large_numbers():
    assert add(1_000_000, 2_000_000) == 3_000_000
