from rest_framework.status import HTTP_404_NOT_FOUND

from iwsoj.views import home


def test_home_404():
    assert home(None).status_code == HTTP_404_NOT_FOUND
