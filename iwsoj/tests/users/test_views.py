from django.http import HttpRequest

from users.views import register


def test_register_invalid_request():
    r = HttpRequest()
    r.DATA = {}
    resp = register(r)
    assert resp.status_code == 400
