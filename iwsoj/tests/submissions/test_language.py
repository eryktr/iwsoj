from submissions.language import Language


def test_choices():
    assert Language.choices() == (('C', 'C'), ('C++', 'CPP'), ('GO', 'GO'), ('Python', 'PYTHON'), ('Java', 'JAVA'))


def test_tostring():
    assert Language.from_string("Java") == Language.JAVA
    # we will NEVER add ada support
    assert Language.from_string("Ada") is None


def test_enum_eq():
    assert Language.GO.get_suffix() == "go"
