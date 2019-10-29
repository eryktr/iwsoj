import pytest

from rest_framework.test import force_authenticate, APIRequestFactory
from submissions.api import SubmissionViewSet
from rest_framework.status import HTTP_201_CREATED, HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_api_submissions(valid_user_serializer, valid_task_serializer):
    user = valid_user_serializer.save()
    task = valid_task_serializer.save()

    data = {
        "task": task.id,
        "language": "Java",
        "sourceCode": "Some test code"
    }

    factory = APIRequestFactory()

    view = SubmissionViewSet.as_view({'post': 'create', 'get': 'retrieve'})

    request = factory.post("/api/submissions/", data=data)
    force_authenticate(request, user=user)
    response=view(request)
    assert response.status_code == HTTP_201_CREATED
    submission_id = response.data['id']

    request = factory.get("/api/submissions/" + submission_id + "/")
    force_authenticate(request, user=user)
    response=view(request, pk=submission_id)
    assert response.data['sourceCode'] == data['sourceCode']


@pytest.mark.django_db
def test_acess_denied():
    factory = APIRequestFactory()
    view = SubmissionViewSet.as_view({'post': 'create', 'get': 'retrieve'})

    request = factory.post("/api/submissions/")
    response = view(request)
    assert response.status_code == HTTP_401_UNAUTHORIZED
