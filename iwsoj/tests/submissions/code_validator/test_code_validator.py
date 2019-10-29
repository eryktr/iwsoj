import pytest

from rest_framework.test import force_authenticate, APIRequestFactory
from submissions.api import SubmissionViewSet
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED

from submissions.status import Status
from tasks.models import Task
from submissions.code_validator.code_validator import validate_code


def test_code_validator_ok(valid_task_data, valid_cpp_code):
    task = Task(**valid_task_data)
    out = validate_code(valid_cpp_code, "C++", task)
    assert out[0] == Status.OK


def test_code_validator_wrong(valid_task_data, wrong_cpp_code):
    task = Task(**valid_task_data)
    out = validate_code(wrong_cpp_code, "C++", task)
    assert out[0] == Status.WA


def test_code_comile_error(valid_task_data, not_compiling_cpp_code):
    task = Task(**valid_task_data)
    out = validate_code(not_compiling_cpp_code, "C++", task)
    assert out[0] == Status.CE and len(out) > 1
