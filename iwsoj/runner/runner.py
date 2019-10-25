import os
import enum
import docker
import shutil
import logging
import tempfile

from collections import Mapping
from pathlib import Path
from typing import Any

from runner.error import UnsupportedLangError

_logger = logging.getLogger(__name__)


class Lang(enum.Enum):
    C = enum.auto()
    Cpp = enum.auto()
    Java = enum.auto()
    Py3 = enum.auto()
    Go = enum.auto()

    @classmethod
    def from_file(cls, codefpath: str) -> Any:
        """
        :param codefpath: The path to the source file. The path must be fully resolved and contain no dots other than the
        target language extension.
        :return: The enum value corresponding to the language that matches the extension
        """
        ext = codefpath.split(".")[1]

        _extmap: Mapping[str, Lang] = {
            "c": cls.C,
            "cpp": cls.Cpp,
            "java": cls.Java,
            "py": cls.Py3,
            "go": cls.Go
        }

        try:
            return _extmap[ext]
        except KeyError:
            raise UnsupportedLangError(codefpath)

    def tostring(self):
        return next(name for name, val in Lang.__members__.items() if val.value == self.value)


def get_dockerfile_dir(lang: Lang) -> str:
    return str(Path(__file__).parent / 'imgs' / lang.tostring().lower())


def ctx2cwd(dockerfile_path) -> None:
    """
    Copies the context of the build process
    into the current working directory
    :param dockerfile_path: The path to the directory containing dockerfile
    """

    for f in os.listdir(dockerfile_path):
        shutil.copy2(f, os.path.dirname(__file__))


def ctxcleanup():
    pass


def soSorryYouLose(codefpath: str) -> str:
    """
    Executes the
    :param codefpath: The path to the code to be run
    :return: stdout of both the compile and the run step of the file in question
    """

    imagetag = "runner"

    _logger.setLevel(logging.INFO)

    lang = Lang.from_file(codefpath)

    dockerfile_path = get_dockerfile_dir(lang)

    _logger.error("Establishing connection to the docker client")
    dockerc = docker.from_env()

    try:
        _logger.error("Building container image...")
        dockerc.images.build(path=".", buildargs={"fpath": codefpath}, tag=imagetag, rm=1)
    finally:

        _logger.info("Executing the solution...")

    return dockerc.containers.run(imagetag)
