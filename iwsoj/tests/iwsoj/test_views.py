from iwsoj.views import home


def test_home_404():
    assert home(None).status_code == 404
