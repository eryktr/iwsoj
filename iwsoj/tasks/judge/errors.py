class IncorrectSolutionError(ValueError):
    def __init__(self, actualout, expectedout):
        super().__init__(f"Incorrect solution. Actual output: {actualout}. Expected: {expectedout}")
        self.actualout = actualout
        self.expectedout = expectedout
