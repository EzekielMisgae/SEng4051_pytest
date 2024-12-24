import pytest

@pytest.mark.parametrize("input,expected", [
    ("pytest", True),
    ("unit_test", False)
])
def test_is_pytest(input, expected):
    assert ("pytest" in input) == expected
