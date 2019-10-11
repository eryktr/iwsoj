import pytest
from django.core.exceptions import ValidationError
from django.utils import timezone


def test_create_date(emptytask):
    cd = emptytask.createdate
    now = timezone.now()
    assert (cd.year, cd.month, cd.day, cd.hour, cd.minute, cd.second) == \
           (now.year, now.month, now.day, now.hour, now.minute, now.second)


def test_emptytask_wont_validate(emptytask):
    with pytest.raises(ValidationError):
        emptytask.full_clean()


def test_invalid_complexity_wont_validates(emptytask):
    emptytask.complexity = 20
    with pytest.raises(ValidationError):
        emptytask.full_clean()
