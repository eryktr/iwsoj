import json

from rest_framework.renderers import JSONRenderer


def test_serializer_valid_task_definition(validserializer, validtask):
    j = JSONRenderer().render(validserializer.data)
    obj = json.loads(j)
    assert obj["definition"] == validtask.definition


def test_json_has_valid_fields(validserializer, validtask):
    j = JSONRenderer().render(validserializer.data)
    obj = json.loads(j)
    for attr in [a for a in validtask.__dict__ if not a.startswith("_")]:
        assert attr in obj
