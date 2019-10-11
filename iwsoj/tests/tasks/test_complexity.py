from tasks.complexity import Complexity


def test_choices():
    assert Complexity.choices() == (("EASY", 1), ("MEDIUM", 2), ("HARD", 3), ("COMPETITIVE", 4))


def test_tostring():
    assert Complexity.tostring(2) == "MEDIUM"


def test_enum_eq():
    assert Complexity.EASY == 1