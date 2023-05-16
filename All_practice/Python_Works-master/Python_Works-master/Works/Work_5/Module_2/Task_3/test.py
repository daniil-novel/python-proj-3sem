import pytest
from bucketsort import bucketsort


@pytest.mark.parametrize("input_str, expected_output", [
    ("1 2 3 4 5", [1, 2, 3, 4, 5]),
    ("3 3 3 3 3", [3, 3, 3, 3, 3]),
    ("5 4 3 2 1", [1, 2, 3, 4, 5]),
])
def test_bucketsort(input_str, expected_output, monkeypatch):
    monkeypatch.setattr('builtins.input', lambda: input_str)
    assert bucketsort() == expected_output
