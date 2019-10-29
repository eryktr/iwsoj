import json

import pytest

from tasks.models import Task


@pytest.fixture()
def emptytask():
    return Task()

@pytest.fixture()
def validtask():
    data = get_valid_task_data()
    t = Task()
    t.input = data['input']
    t.output = data['output']
    t.statement = data['statement']
    t.title = data['title']
    return t


def get_valid_task_data():
    return {
        "title": "Simple task",
        "statement": "Solve me if u dare",
        "complexity": 2,
        "input": "InputLine[1]\nInputLine[2]",
        "output": "OutputLine[0]\nOutputLine[1]"
    }

