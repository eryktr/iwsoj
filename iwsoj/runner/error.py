class UnsupportedLangError(ValueError):
    FAIL_MSG = "The {} extension is currently not supported."

    def __init__(self, lang: str):
        super().__init__(self.FAIL_MSG.format(lang))


class InvalidPathError(ValueError):
    FAIL_MSG = "Invalid path: {}"

    def __init__(self, path: str):
        super().__init__(self.FAIL_MSG.format(path))


class PathTooLongError(InvalidPathError):
    FAIL_MSG = "Path too long: {}"


class CompilationError(ValueError):
    pass
