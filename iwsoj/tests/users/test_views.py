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
def test_register_ok(mocker, validated_data: dict):
	mocker.patch.object(User, "save")
	request = HttpRequest()
	request.DATA = validated_data
	request.method = 'POST'
	request.POST = {'id': '1', 'title': 'What?', 'statement': 'abcd', 
	'createdate': '2019-10-17 11:11:11', 'complexity': '1', 'definition': 'ghi'}
	serialized = UserSerializer(data=request.DATA)
	resp = register(request)
	assert resp.status_code == HTTP_201_CREATED