import pytest_tutorial.main as main
import pytest


@pytest.mark.parametrize(
    "num, expected",
    [
        (1, False),
        (2, True),
        (3, True),
        (4, False),
        (5, True),
        (6, False),
        (7, True),
        (8, False),
        (9, False),
        (10, False),
        (11, True),
        (12, False),
    ],
)
def test_is_prime(num, expected):
    assert main.is_prime(num) == expected
