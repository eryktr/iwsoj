import pytest

from submissions.serializers.submission_serializer import SubmissionSerializer


@pytest.fixture()
def validserializer(valid_submission):
    return SubmissionSerializer(valid_submission)
