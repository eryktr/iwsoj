import pytest
from django.test import Client
from rest_framework.status import HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_200_OK


@pytest.mark.django_db
def test_register_rejected():
	client = Client()
	resp = client.post("/api/register/", data=None)
	assert resp.status_code == HTTP_400_BAD_REQUEST

@pytest.mark.django_db
def test_register_login_ok(validated_data: dict):
	client = Client()
	resp = client.post("/api/register/", data=validated_data)
	assert resp.status_code == HTTP_201_CREATED
	user = validated_data['username']
	passwd = validated_data['password']
	resp = client.post("/api/token_auth/", data={"username": user, "password": passwd})
	assert 'token' in resp.data
	assert resp.status_code == HTTP_200_OK

@pytest.mark.django_db
def test_login_rejected(validated_data: dict):
	client = Client()
	client.post("/api/register/", data=validated_data)
	user = validated_data['username']
	resp = client.post("/api/token_auth/", data={"username": user, "password": "SomeWrongPassword"})
	assert resp.status_code == HTTP_400_BAD_REQUEST
