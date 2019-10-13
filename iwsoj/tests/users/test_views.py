from users.views import register


def test_register_invalid_request():
    resp = register(None)
    assert resp.status_code == 400
