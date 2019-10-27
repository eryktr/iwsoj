import json
import pytest

from rest_framework.renderers import JSONRenderer


@pytest.mark.django_db
def test_serializer_valid_submission_source_code(validserializer, valid_submission):
    j = JSONRenderer().render(validserializer.data)
    print(j)
    obj = json.loads(j)
    assert obj["sourceCode"] == valid_submission.sourceCode

