import pytest_tutorial.main as main
import pytest

@pytest.fixture
def db():
    """Provide fresh db instance"""
    database = main.Database()
    yield database
    database.data.clear() # Clean db after use

def test_add_user_db(db):
    db.add_user(1, 'Alice')
    assert db.get_user(1) == "Alice"

def test_add_duplicate_user_db(db):
    db.add_user(1, 'Alice')
    with pytest.raises(ValueError, match="User already exists"):
        db.add_user(1, 'Bob')

def test_delete_user_db(db):
    db.add_user(2, 'Bob')
    db.delete_user(2)
    assert db.get_user(2) is None

