import enum


class Status(enum.Enum):
    OK = "Passed"
    REJECTED = "Rejected"
    PENDING = "Pending"

    @classmethod
    def choices(cls):
        return tuple((i.value, i.name) for i in cls)
