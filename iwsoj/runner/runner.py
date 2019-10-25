import enum
from collections import Mapping
from pathlib import Path
from typing import Any

from runner.error import UnsupportedLangError


class Lang(enum.Enum):
    C = enum.auto()
    Cpp = enum.auto()
    Java = enum.auto()
    Py3 = enum.auto()
    Go = enum.auto()

    @classmethod
    def from_file(cls, fpath: str) -> Any:
        """
        :param The path to the source file. The path must be fully resolved and contain no dots other than the
        target language extension.
        :return: The enum value corresponding to the language that matches the extension
        """
        ext = fpath.split(".")[1]

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
            raise UnsupportedLangError(fpath)

    def tostring(self):
        return next(name for name, val in Lang.__members__.items() if val.value == self.value)


def get_dockerfile_path(lang: Lang) -> str:
    return Path(__file__).parent / 'imgs' / lang.tostring().lower() / 'Dockerfile'


def runcode(fpath):
    lang = Lang.from_file(fpath)
    dockerfile_path = get_dockerfile_path(lang)
