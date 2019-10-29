from tasks.complexity import Complexity


def test_choices():
    assert Complexity.choices() == ((1, 'EASY'), (2, 'MEDIUM'), (3, 'HARD'), (4, 'COMPETITIVE'))


def test_tostring():
    assert Complexity.tostring(2) == "MEDIUM"


def test_enum_eq():
    assert Complexity.EASY == 1