import pytest_tutorial.main as main
import pytest
    
@pytest.fixture
def user_manager() -> main.UserManager:
    """Create fresh user"""
    return main.UserManager()

def test_add_user_manager(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") is True
    assert user_manager.get_user("john_doe") == "john@example.com"

def test_add_duplicate_user_manager(user_manager):
    assert user_manager.add_user("john_doe", "john@example.com") is True
    with pytest.raises(ValueError, match="User already exists"):
        assert user_manager.add_user("john_doe", "john@example.com")