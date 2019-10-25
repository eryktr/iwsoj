import enum


class Complexity(enum.IntEnum):
    EASY = 1
    MEDIUM = 2
    HARD = 3
    COMPETITIVE = 4

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)

    @classmethod
    def tostring(cls, val):
        return next(filter(lambda x: x[0] == val, cls.choices()))[1]
