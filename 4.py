import pytest

def add_numbers(a, b):
    return a + b

def test_addition():
    result = add_numbers(2, 3)
    assert result == 5

def test_subtraction():
    result = add_numbers(5, 3)
    assert result == 2
