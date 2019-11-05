class UnsupportedLangError(ValueError):
    FAIL_MSG = "The {} extension is currently not supported."

    def __init__(self, lang: str):
        super().__init__(self.FAIL_MSG.format(lang))


class AbstractError(ValueError):
    FAIL_MSG = ""

    def __init__(self):
        super().__init__(self.FAIL_MSG)


class InvalidPathError(AbstractError):
    FAIL_MSG = "Invalid path: {}"

    def __init__(self, path: str):
        self.FAIL_MSG = self.FAIL_MSG.format(path)
        super().__init__()


class PathTooLongError(AbstractError):
    FAIL_MSG = "Path too long: {}"

    def __init__(self, path: str):
        self.FAIL_MSG = self.FAIL_MSG.format(path)
        super().__init__()


class CompilationError(ValueError):
    pass


class TimeoutError(AbstractError):
    FAIL_MSG = "Timed out."


class OutOfMemoryError(AbstractError):
    FAIL_MSG = "Memory limit exceeded."
