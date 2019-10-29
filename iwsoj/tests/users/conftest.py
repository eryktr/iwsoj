import pytest


@pytest.fixture()
def validated_data():
    return {
        "username": "testuser",
        "password": "testpassword12!",
        "first_name": "firstname",
        "last_name": "lastname",
        "email": "email.email@email.com",
    }