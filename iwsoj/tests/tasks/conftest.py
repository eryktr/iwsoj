import pytest

from tasks.models import Task


@pytest.fixture()
def emptytask():
    return Task()
