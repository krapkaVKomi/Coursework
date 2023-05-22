@pytest.mark.parametrize("number", [2, 4, 6])
def test_is_even(number):
    assert number % 2 == 0
