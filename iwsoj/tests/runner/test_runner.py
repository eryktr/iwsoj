from pathlib import Path

import os
import pytest
from docker.errors import ContainerError

from runner.error import UnsupportedLangError, CompilationError
from runner.runner import Lang, get_dockerfile_dir, soSorryYouLose

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
    sep = os.sep
    assert get_dockerfile_dir(Lang.C).endswith("iwsoj" + sep + "runner" + sep + "imgs" + sep + "c")


dummypath = Path.cwd() / 'runner' / 'dummy'


@pytest.mark.integration
def test_runner_c_ok():
    assert soSorryYouLose(str(dummypath / 'dummy.c')) == "It takes 8 bits to represent 222\n"


@pytest.mark.integration
def test_runner_cpp_ok():
    assert soSorryYouLose(str(dummypath / 'dummy.cpp')) == "Distance from p1 and p2 is 0\n"


@pytest.mark.integration
def test_runner_py3_ok():
    assert soSorryYouLose(str(dummypath / 'dummy.py')) == "The 10th Fib number is 55\n"


@pytest.mark.integration
def test_runner_java_ok():
    assert soSorryYouLose(str(dummypath / 'dummy.java')) == "Factorial of 4 is 24\n"


@pytest.mark.integration
def test_runner_go_ok():
    assert soSorryYouLose(str(dummypath / 'dummy.go')) == "GO somewhere else!\n"

@pytest.mark.integration
def test_runner_c_stdin_ok():
    assert soSorryYouLose(str(dummypath / 'dummy_stdin.c')) == "It takes 8 bits to represent 220\n"

@pytest.mark.integration
def test_runner_compile_error():
    try:
        print(soSorryYouLose(str(dummypath / 'dummy_iwontcompile.c')))
    except ContainerError as err:
        assert 1