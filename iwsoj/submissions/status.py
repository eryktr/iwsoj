import enum


class Status(enum.Enum):
    OK = "Passed"
    WA = "Wrong answer"
    MLE = "Memory limit exceeded"
    RE = "Runtime error"
    TLE = "Time limit exceeded"
    CE = "Compilation error"
    IE = "Internal system error"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)
