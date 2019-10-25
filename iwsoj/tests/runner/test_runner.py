import pytest

from runner.error import UnsupportedLangError
from runner.runner import Lang, get_dockerfile_dir


def test_lang_fromfile_ok():
    assert Lang.from_file("helloworld.c") is Lang.C
    assert Lang.from_file("byeworld.py") is Lang.Py3


def test_lang_fromfile_unsupported():
    with pytest.raises(UnsupportedLangError):
        Lang.from_file("omgwhoousesada.ada")


def test_lang_tostring():
    py = Lang.Py3
    assert py.tostring() == "Py3"


def test_get_dockerfile_dir():
    assert get_dockerfile_dir(Lang.C).endswith("iwsoj/runner/imgs/c")
