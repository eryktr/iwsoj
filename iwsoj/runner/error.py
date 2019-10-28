class UnsupportedLangError(ValueError):
    FAIL_MSG = "The {} extension is currently not supported."

    def __init__(self, lang: str):
        super().__init__(self.FAIL_MSG.format(lang))
