import pytest

from submissions.models import Submission
from tasks.serializers.task_serializer import TaskSerializer
from users.serializers.user_serializer import UserSerializer


@pytest.fixture()
def valid_submission(valid_submission_data):
    return Submission(**valid_submission_data)


@pytest.fixture()
def valid_submission_data(valid_task_serializer, valid_user_serializer):
    valid_task = valid_task_serializer.save()
    valid_user = valid_user_serializer.save()
    return {
        "user": valid_user,
        "task": valid_task,
        "language": "Java",
        "sourceCode": "This code causes a compilation error"
    }


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
    return {
        "title": "Simple task",
        "statement": "Multiply by two!",
        "complexity": 2,
        "input": "1 input",
        "output": "2 output"
    }



