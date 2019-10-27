import json

import pytest
from django.contrib.auth.models import User

from submissions.models import Submission
from submissions.serializers.submission_serializer import SubmissionSerializer
from tasks.models import Task
from tasks.serializers.task_serializer import TaskSerializer
from users.serializers.user_serializer import UserSerializer


@pytest.fixture()
def valid_submission(valid_task_serializer, valid_user_serializer):
    valid_task = valid_task_serializer.save()
    valid_user = valid_user_serializer.save()
    data = {
        "user": valid_user,
        "task": valid_task,
        "language": "Java",
        "sourceCode": "This code causes a compilation error"
    }
    return Submission(**data)


@pytest.fixture()
def valid_user_serializer(valid_user_data):
    user_ser = UserSerializer(data=valid_user_data)
    assert user_ser.is_valid()
    return user_ser


@pytest.fixture()
def valid_task_serializer(valid_task_data):
    task_ser = TaskSerializer(data=valid_task_data)
    assert task_ser.is_valid()
    return task_ser


@pytest.fixture()
def valid_user_data():
    return {
        "username": "testuser",
        "password": "testpassword12!",
        "first_name": "firstname",
        "last_name": "lastname",
        "email": "email.email@email.com",
    }



@pytest.fixture()
def valid_task_data():
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



