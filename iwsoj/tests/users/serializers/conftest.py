import pytest

from users.serializers.user_serializer import UserSerializer


@pytest.fixture()
def validated_data():
    return {
        "username": "testuser",
        "password": "Testpassword12!",
        "first_name": "firstname",
        "last_name": "lastname",
        "email": "email.email@email.com",
    }


@pytest.fixture()
def mocked_serializer(mocker):
    us = UserSerializer()
    mocker.patch.object(us, "_save_user", autospec=True)
    return us
