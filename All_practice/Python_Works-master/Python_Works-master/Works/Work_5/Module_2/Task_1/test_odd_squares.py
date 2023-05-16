import pytest
from main import get_odd_squares


@pytest.fixture
def not_a_list():
    return "not a list"


@pytest.fixture
def not_numbers():
    return ["abc", 1, "def", 3.14]


@pytest.mark.parametrize("input_list, expected_output", [
    ([], []),
    ([1, 2, 3], [1, 9]),
    ([0, 2, 4], []),
    ([-1, -2, -3], [1, 9])
])
def test_get_odd_squares(input_list, expected_output):
    assert get_odd_squares(input_list) == expected_output


def test_get_odd_squares_type_error(not_a_list):
    with pytest.raises(TypeError):
        get_odd_squares(not_a_list)


def test_get_odd_squares_value_error(not_numbers):
    with pytest.raises(ValueError):
        get_odd_squares(not_numbers)
