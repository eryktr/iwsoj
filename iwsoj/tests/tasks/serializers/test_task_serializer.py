import json

from rest_framework.renderers import JSONRenderer


def test_serializer_valid_task_definition(validserializer, validtask):
    j = JSONRenderer().render(validserializer.data)
    print(j)
    obj = json.loads(j)
    assert obj["statement"] == validtask.statement
