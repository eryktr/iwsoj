import enum
from collections import Mapping


class Language(enum.Enum):
    C = "C"
    CPP = "C++"
    GO = "GO"
    PYTHON = "Python"
    JAVA = "Java"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

    @classmethod
    def from_string(cls, name):
        for i in cls:
            if (i.value == name):
                return i
        return None

    def get_suffix(self):

        _extmap: Mapping[Language, str] = {
            Language.C : "c",
            Language.CPP : "cpp",
            Language.JAVA: "java",
            Language.GO: "go",
            Language.PYTHON: "py"
        }
        return _extmap.get(self)


