from builtins import FileNotFoundError
from pathlib import Path

import os
import pytest
from docker.errors import ContainerError

from runner.error import UnsupportedLangError, InvalidPathError, PathTooLongError, TimeoutError, OutOfMemoryError
from runner.runner import Lang, get_dockerfile_dir, soSorryYouLose


@pytest.mark.parametrize("string, lang",
                         [("helloworld.c", Lang.C), ("byeworld.py", Lang.Py3), ("plsno.java", Lang.Java),
                          ("csharp.cpp", Lang.Cpp), ("goaway.go", Lang.Go), ("/complex/path/to/file.go", Lang.Go)])
def test_lang_fromfile_ok(string, lang):
    assert Lang.from_file(string) is lang


def test_lang_fromfile_unsupported():
    with pytest.raises(UnsupportedLangError) as err:
        Lang.from_file("omgwhoousesada.ada")
    assert str(err.value) == f"The .ada extension is currently not supported."


def test_lang_fromfile_invalidpath():
    pth = "/i/know/that/i.wont.work.cpp"
    with pytest.raises(InvalidPathError) as err:
        Lang.from_file(pth)
    assert str(err.value) == f"Invalid path: {pth}"


def test_lang_fromfile_path_too_long():
    pth = "/wtfisthat" * 100 + ".java"
    with pytest.raises(PathTooLongError) as err:
        Lang.from_file(pth)
    assert str(err.value) == f"Path too long: {pth}"


@pytest.mark.parametrize("lang, string",
                         [(Lang.Py3, "Py3"), (Lang.Go, "Go"), (Lang.Cpp, "Cpp"), (Lang.C, "C"), (Lang.Java, "Java")])
def test_lang_tostring(lang, string):
    assert lang.tostring() == string


sep = os.sep
basepath = f"iwsoj{sep}runner{sep}imgs"
ending = lambda l: f"{basepath}{sep}{l}"


@pytest.mark.parametrize("lang, end", [(Lang.C, ending("c")), (Lang.Cpp, ending("cpp")), (Lang.Java, ending("java")),
                                       (Lang.Go, ending("go")), (Lang.Py3, ending("py3"))])
def test_get_dockerfile_dir(lang, end):
    assert get_dockerfile_dir(lang).endswith(end)


dummypath = Path.cwd() / 'runner' / 'dummy'


@pytest.mark.integration
def test_runner_fails_code_file_doesnt_exist():
    with pytest.raises(FileNotFoundError):
        soSorryYouLose("/path/to/nowhere.c", str(dummypath / 'dummy_input.txt'))


@pytest.mark.integration
def test_runner_fails_stdin_file_doesnt_exist():
    with pytest.raises(FileNotFoundError):
        soSorryYouLose(str(dummypath / 'dummy.c'), "/path/to/nowhere.txt")


@pytest.mark.parametrize("path", ["/path/to/dir", "a" * 400 + ".c", "a.b.c", "/path/app.kt", "", "~"])
@pytest.mark.integration
def test_runner_fails_for_invalid_path(path):
    with pytest.raises(ValueError):
        soSorryYouLose(path, str(dummypath / 'dummy_input.txt'))


@pytest.mark.integration
def test_runner_c_ok():
    assert soSorryYouLose(str(dummypath / 'dummy.c'),
                          str(dummypath / "dummy_input.txt")) == "It takes 8 bits to represent 222\n"


@pytest.mark.integration
def test_runner_cpp_ok():
    assert soSorryYouLose(str(dummypath / 'dummy.cpp'),
                          str(dummypath / "dummy_input.txt")) == "Distance from p1 and p2 is 0\n"


@pytest.mark.integration
def test_runner_py3_ok():
    assert soSorryYouLose(str(dummypath / 'dummy.py'),
                          str(dummypath / "dummy_input.txt")) == "The 10th Fib number is 55\n"


@pytest.mark.integration
def test_runner_java_ok():
    assert soSorryYouLose(str(dummypath / 'dummy.java'), str(dummypath / "dummy_input.txt")) == "Factorial of 4 is 24\n"


@pytest.mark.integration
def test_runner_go_ok():
    assert soSorryYouLose(str(dummypath / 'dummy.go'), str(dummypath / 'dummy_input.txt')) == "GO somewhere else!\n"


@pytest.mark.integration
def test_runner_c_stdin_ok():
    assert soSorryYouLose(str(dummypath / 'dummy_stdin.c'),
                          str(dummypath / 'dummy_input.txt')) == "It takes 8 bits to represent 220\n"


@pytest.mark.integration
def test_runner_compile_error():
    try:
        print(soSorryYouLose(str(dummypath / 'dummy_iwontcompile.c'), str(dummypath / 'dummy_input.txt')))
    except ContainerError as err:
        assert 1


@pytest.mark.integration
def test_runner_timeout():
    codefpath = str(dummypath / 'goodnight.py')
    with pytest.raises(TimeoutError) as err:
        soSorryYouLose(codefpath, str(dummypath / 'dummy_input.txt'), time_limit=1.0)
    assert str(err.value) == TimeoutError.FAIL_MSG


@pytest.mark.integration
def test_runner_out_of_mem():
    codefpath = str(dummypath / 'heavyone.py')
    with pytest.raises(OutOfMemoryError) as err:
        soSorryYouLose(codefpath, str(dummypath / 'dummy_input.txt'), mem_limit="4m", time_limit=100)
    assert str(err.value) == OutOfMemoryError.FAIL_MSG
