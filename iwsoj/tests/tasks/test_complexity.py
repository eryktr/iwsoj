from tasks.complexity import Complexity


def test_choices():
    assert Complexity.choices() == (("EASY", 1), ("MEDIUM", 2), ("HARD", 3), ("COMPETITIVE", 4))
