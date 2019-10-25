import json

import pytest

from tasks.models import Task

@pytest.fixture()
def validated_user_data():
    return {
        "username": "testuser",
        "password": "testpassword12!",
        "first_name": "firstname",
        "last_name": "lastname",
        "email": "email.email@email.com",
    }

@pytest.fixture()
def emptytask():
    return Task()

@pytest.fixture()
def validtask():
    data = get_valid_task_data()
    t = Task()
    t.definition = data['definition']
    t.statement = data['statement']
    t.title = data['title']
    return t

@pytest.fixture()
def valid_task_data():
    return get_valid_task_data()

def get_valid_task_data():
    definition = json.dumps({
        "inputLines": [
            "InputLine[1]",
            "InputLine[2]"
        ],
        "outputLines": [
            "OutputLine[0]",
            "OutputLine[1]"
        ]
    })

    return {
        "title": "Simple task",
        "statement": "Solve me if u dare",
        "complexity": 2,
        "definition": definition
    }

