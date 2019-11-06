import os
import enum
import subprocess

import docker
import shutil
import logging

from collections import Mapping
from pathlib import Path
from typing import Any, Union, Optional, Dict

from docker.errors import ContainerError, ImageNotFound

from runner.error import UnsupportedLangError, InvalidPathError, PathTooLongError, TimeoutError, OutOfMemoryError

logging.basicConfig()
_logger = logging.getLogger(__name__)
_logger.setLevel(logging.INFO)
_docker = docker.from_env()

ALREADY_BUILT: bool = False


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
            raise UnsupportedLangError("." + codefpath.split(".")[-1])

    def tostring(self):
        return next(name for name, val in Lang.__members__.items() if val.value == self.value)


image_tags: Dict[Lang, str] = {
    Lang.C: "iwsojc",
    Lang.Py3: "iwsojpy",
    Lang.Java: "iwsojjunk",
    Lang.Cpp: "iwsojcpp",
    Lang.Go: "onetoruleall"
}


extensions: Dict[Lang, str] = {
    Lang.C: ".c",
    Lang.Py3: ".py",
    Lang.Java: ".java",
    Lang.Cpp: ".cpp",
    Lang.Go: ".go"
}


def images_already_built() -> bool:
    # Yes there really is no better way but to use
    # a named fifo
    global ALREADY_BUILT
    pipe = subprocess.Popen(["docker", "image", "ls"], stdout=subprocess.PIPE)
    out = pipe.communicate()
    built = all([tag in out for tag in image_tags.values()])
    ALREADY_BUILT = ALREADY_BUILT or built
    return built


def build_images() -> None:
    """
    This method takes some time to execute, yet gives an enormous
    boost in terms of future executions.
    """
    global ALREADY_BUILT
    for lang, tag in image_tags.items():
        dockerfile = os.path.join(get_dockerfile_dir(lang), "Dockerfile")
        dockerfile_path_cwd = os.path.join(os.getcwd(), "Dockerfile")
        shutil.copy2(dockerfile, dockerfile_path_cwd)
        _docker.images.build(path=os.getcwd(), tag=tag, rm=True)
    ALREADY_BUILT = True
    os.remove(os.path.join(os.getcwd(), "Dockerfile"))


def get_tag(lang: Lang) -> Optional[str]:
    return image_tags.get(lang)


def get_dockerfile_dir(lang: Lang) -> str:
    return str(Path(__file__).parent / 'imgs' / lang.tostring().lower())


def get_volume_path(lang: Lang):
    return str(Path.cwd() / "volume" / lang.tostring().lower())


def ctx2cwd(volume_path, codefile_path, stdinfile_path, ext) -> None:
    """
    Copies the context of the build process
    into the current working directory
    :param volume_path: The path to the volume mapping to the selected lang
    :param codefile_path: The path to the source file
    :param stdinfile_path: The path to the file containing the input to the program
    """
    codefname = os.path.basename(codefile_path)
    stdinfname = os.path.basename(stdinfile_path)
    target_codef = os.path.join(volume_path, codefname)
    target_stdinf = os.path.join(volume_path, stdinfname)
    shutil.copy(codefile_path, volume_path)
    shutil.copy(stdinfile_path, volume_path)
    os.rename(target_codef, os.path.join(volume_path, f"target{ext}"))
    os.rename(target_stdinf, os.path.join(volume_path, "input.txt"))


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


def soSorryYouLose(codefpath: str, stdinfpath: str, mem_limit: str = "256m",
                   time_limit: Union[float, None] = None) -> str:
    """
    Executes the
    :param codefpath: The path to the code to be run
    :param stdinfpath: The path to the input file
    :param mem_limit: The memory limit of the script, e.g. 128m, 32k, 2g
    :param time_limit: Maximum number of seconds (as a float) that the program can run, e.g. 2.5, 7.0
    :return: stdout of both the compile and the run step of the file in question
    """
    if not images_already_built():
        build_images()
    lang = Lang.from_file(codefpath)
    imagetag = get_tag(lang)
    ext = extensions[lang]
    vol = get_volume_path(lang)
    try:
        ctx2cwd(vol, codefpath, stdinfpath, ext)
        volumes = {
            vol: {
                "bind": "/runner",
                "mode": "rw"
            }
        }
        cmd = (f"timeout {time_limit}" if time_limit else '') + " /runner/run.sh"
        info = _docker.containers.run(imagetag, mem_limit=mem_limit, command=cmd, volumes=volumes)
        return info.decode("utf8")
    except ContainerError as err:
        if err.exit_status == 124:
            raise TimeoutError()
        if err.exit_status == 137:
            raise OutOfMemoryError()
        else:
            raise err
