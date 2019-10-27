import enum


class Language(enum.Enum):
    C = "C"
    CPP = "C++"
    GO = "GO"
    PYTHON = "Python"
    JAVA = "Java"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

