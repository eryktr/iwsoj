import pytest
from django.contrib.auth.models import User
from django.db import IntegrityError

from users.serializers.user_serializer import UserSerializer


def test_create_valid_data(mocked_serializer: UserSerializer, validated_data: dict, mocker):
    mocker.patch.object(User, "save")
    u = mocked_serializer.create(validated_data)
    assert u.first_name == validated_data["first_name"]
    assert u.last_name == validated_data["last_name"]
    assert u.username == validated_data["username"]


def test_create_valid_data_save_called(validated_data: dict, mocker):
    us = UserSerializer(validated_data)
    mocker.patch.object(User, "save")
    u = us.create(validated_data)
    assert u.save.call_count == 2  # Called once on model instantiation and once by the serializer


@pytest.mark.django_db
def test_serializer_is_valid_for_valid_data(validated_data: dict):
    us = UserSerializer(data=validated_data)
    assert us.is_valid()


@pytest.mark.django_db
def test_serializer_only_unique_users(validated_data):
    us = UserSerializer()
    u = us.create(validated_data)
    with pytest.raises(IntegrityError):
        u = us.create(validated_data)
