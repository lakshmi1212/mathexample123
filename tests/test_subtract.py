import pytest
from src.math_operations import subtract

def test_subtract_positive_numbers():
    assert subtract(5, 3) == 2

def test_subtract_negative_numbers():
    assert subtract(-5, -3) == -2

def test_subtract_mixed_sign_numbers():
    assert subtract(-5, 3) == -8
    assert subtract(5, -3) == 8

def test_subtract_zero():
    assert subtract(0, 0) == 0
    assert subtract(0, 5) == -5
    assert subtract(5, 0) == 5

def test_subtract_large_numbers():
    assert subtract(2000000, 1000000) == 1000000

def test_subtract_float_numbers():
    assert subtract(5.6, 2.1) == pytest.approx(3.5)

def test_subtract_type_error():
    with pytest.raises(TypeError):
        subtract('a', 1)
    with pytest.raises(TypeError):
        subtract(1, 'b')
