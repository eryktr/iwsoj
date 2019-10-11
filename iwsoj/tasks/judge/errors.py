INCORRECT_SOLUTION = "Incorrect solution. Actual output: {}. Expected: {}".format

class IncorrectSolutionError(ValueError):
    def __init__(self, actualout, expectedout):
        super().__init__(INCORRECT_SOLUTION(actualout, expectedout))
        self.actualout = actualout
        self.expectedout = expectedout
