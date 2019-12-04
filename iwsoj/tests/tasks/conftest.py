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
    t.input_public = data['input_public']
    t.output_public = data['output_public']
    t.input_hidden = data['input_hidden']
    t.output_hidden = data['output_hidden']
    t.statement = data['statement']
    t.title = data['title']
    return t


def get_valid_task_data():
    return {
        "title": "Simple task",
        "statement": "Solve me if u dare",
        "complexity": 2,
        "input_public": "InputLine[1]\nInputLine[2]",
        "output_public": "OutputLine[0]\nOutputLine[1]",
        "input_hidden": "InputLine[1]\nInputLine[2]",
        "output_hidden": "OutputLine[0]\nOutputLine[1]"
    }

