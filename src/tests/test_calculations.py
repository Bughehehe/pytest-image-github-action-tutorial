import pytest_tutorial.main as main
import pytest

def test_add():
    assert main.add(2, 3) == 5
    assert main.add(-1, 1) == 0
    assert main.add(0, 0) == 0
    assert main.add(1.5, 2.25) == 3.75

def test_divide():
    assert main.divide(10, 10) == 1
    assert main.divide(20, -10) == -2
    with pytest.raises(ValueError, match='Cannot divide by zero'):
        main.divide(10, 0)