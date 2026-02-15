import pytest
from src.math_operations import add

def test_add_positive_numbers():
    assert add(2, 3) == 5

def test_add_negative_numbers():
    assert add(-2, -3) == -5

def test_add_mixed_sign_numbers():
    assert add(-2, 3) == 1
    assert add(2, -3) == -1

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_large_numbers():
    assert add(1000000, 2000000) == 3000000

def test_add_float_numbers():
    assert add(2.5, 3.1) == pytest.approx(5.6)

def test_add_type_error():
    with pytest.raises(TypeError):
        add('a', 1)
    with pytest.raises(TypeError):
        add(1, 'b')
