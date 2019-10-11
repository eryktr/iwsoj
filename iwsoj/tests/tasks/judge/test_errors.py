from tasks.judge.errors import IncorrectSolutionError, INCORRECT_SOLUTION


def test_incorrect_solution_error():
    e = IncorrectSolutionError([1], [2])
    assert str(e) == INCORRECT_SOLUTION([1], [2])
