import json
import pytest

from rest_framework.renderers import JSONRenderer
from submissions.serializers.submission_serializer import SubmissionSerializer
from submissions.status import Status


@pytest.mark.django_db
def test_serializer_valid_submission_source_code(validserializer, valid_submission):
    j = JSONRenderer().render(validserializer.data)
    print(j)
    obj = json.loads(j)
    assert obj["sourceCode"] == valid_submission.sourceCode

@pytest.mark.django_db
def test_serializer_compiler_error_valid(mocker, valid_submission_data):
    ss = SubmissionSerializer(valid_submission_data)
    mocker.patch.object(ss, "_validate", autospec=True, return_value=(Status.CE, "Compiler error"))
    mocker.patch.object(ss, "_get_user", autospec=True, return_value=valid_submission_data['user'])
    submission = ss.create(valid_submission_data)
    assert submission.language == valid_submission_data['language']
    assert submission.status == Status.CE.value
    assert submission.error == "Compiler error"

@pytest.mark.django_db
def test_serializer_wa(mocker, valid_submission_data):
    ss = SubmissionSerializer(valid_submission_data)
    mocker.patch.object(ss, "_validate", autospec=True, return_value=(Status.WA,"error"))
    mocker.patch.object(ss, "_get_user", autospec=True, return_value=valid_submission_data['user'])
    submission = ss.create(valid_submission_data)
    assert submission.language == valid_submission_data['language']
    assert submission.status == Status.WA.value

