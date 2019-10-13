from django.http import HttpRequest
from rest_framework.status import HTTP_400_BAD_REQUEST

from users.views import register


def test_register_invalid_request():
    r = HttpRequest()
    r.DATA = {}
    resp = register(r)
    assert resp.status_code == HTTP_400_BAD_REQUEST
