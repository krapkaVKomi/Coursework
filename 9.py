import pytest

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (3, 4, 7)])
def test_addition(a, b, expected):
    result = a + b
    assert result == expected
