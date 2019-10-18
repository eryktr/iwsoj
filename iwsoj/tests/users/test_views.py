import pytest
from django.http import HttpRequest
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST
from django.contrib.auth.models import User
from users.serializers.user_serializer import UserSerializer
from users.views import register



def test_register_invalid_request():
    r = HttpRequest()
    r.DATA = {}
    resp = register(r)
    assert resp.status_code == HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_register_ok(mocker, mocked_serializer: UserSerializer, validated_data: dict):
	mocker.patch.object(User, "save")
	r = HttpRequest()
	r.DATA = validated_data
	serialized = mocked_serializer.create(r.DATA)
	resp = register(r)
	assert resp.status_code == HTTP_201_CREATED