import pytest

@pytest.fixture
def setup_data():
    # Підготовка даних для тестування
    data = [1, 2, 3]
    return data

def test_data_length(setup_data):
    assert len(setup_data) == 3

def test_data_sum(setup_data):
    assert sum(setup_data) == 6
