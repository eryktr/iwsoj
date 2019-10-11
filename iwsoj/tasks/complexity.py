import enum


class Complexity(enum.IntEnum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    COMPETITIVE = 4

    @classmethod
    def choices(cls):
        return tuple((i.name, i.value) for i in cls)

    @classmethod
    def tostring(cls, val):
        return next(filter(lambda x: x[1] == val, cls.choices()))[0]
