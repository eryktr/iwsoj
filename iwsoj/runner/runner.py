import os
import enum
import docker
import shutil
import logging

from collections import Mapping
from pathlib import Path
from typing import Any

from runner.error import UnsupportedLangError, InvalidPathError, PathTooLongError

logging.basicConfig()
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)


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
        if len(codefpath) > 255:
            raise PathTooLongError(codefpath)
        split = codefpath.split(".")
        if len(split) != 2:
            raise InvalidPathError(codefpath)
        ext = split[1]

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
            raise UnsupportedLangError("."+codefpath.split(".")[-1])

    def tostring(self):
        return next(name for name, val in Lang.__members__.items() if val.value == self.value)


def get_dockerfile_dir(lang: Lang) -> str:
    return str(Path(__file__).parent / 'imgs' / lang.tostring().lower())


def ctx2cwd(dockerfile_path, codefile_path, stdinfile_path) -> None:
    """
    Copies the context of the build process
    into the current working directory
    :param dockerfile_path: The path to the directory containing dockerfile
    :param codefile_path: The path to the source file
    """

    for f in os.listdir(dockerfile_path):
        shutil.copy2(os.path.join(dockerfile_path, f), os.getcwd())
    shutil.copy2(codefile_path, os.getcwd())
    shutil.copy2(stdinfile_path, os.getcwd())


def cwdctxcleanup(dockerfile_path, codefile_path, stdinfile_path):
    """
    The bigger your understanding of what it does,
    the lower the likelihood that you might use it.
    """
    to_delete = (os.path.basename(f) for f in os.listdir(dockerfile_path))

    for f in to_delete:
        os.remove(os.path.join(os.getcwd(), f))
    os.remove(os.path.join(os.getcwd(), os.path.basename(codefile_path)))
    os.remove(os.path.join(os.getcwd(), os.path.basename(stdinfile_path)))


def soSorryYouLose(codefpath: str, stdinfpath: str) -> str:
    """
    Executes the
    :param codefpath: The path to the code to be run
    :param stdinfpath: The path to the input file
    :return: stdout of both the compile and the run step of the file in question
    """

    imagetag = "runner"
    lang = Lang.from_file(codefpath)

    dockerfile_path = get_dockerfile_dir(lang)
    dockerc = docker.from_env()

    try:
        ctx2cwd(dockerfile_path, codefpath, stdinfpath)
        short_codefname = os.path.basename(codefpath)
        short_stdinfname = os.path.basename(stdinfpath)
        dockerc.images.build(path=os.getcwd(), buildargs={"fpath": short_codefname, "stdinfpath": short_stdinfname}, tag=imagetag, rm=True)
        info = dockerc.containers.run(imagetag, remove=True)
        return info.decode("utf8")

    finally:
        cwdctxcleanup(dockerfile_path, codefpath, stdinfpath)
        dockerc.images.remove(imagetag)
