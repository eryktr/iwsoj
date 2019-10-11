import json

from rest_framework.renderers import JSONRenderer

from tasks.serializers.task_serializer import TaskSerializer


def test_serializer_valid_task_definition(validtask):
    s = TaskSerializer(validtask)
    j = JSONRenderer().render(s.data)
    obj = json.loads(j)
    assert obj["definition"] == validtask.definition


def test_json_has_valid_fields(validtask):
    s = TaskSerializer(validtask)
    j = JSONRenderer().render(s.data)
    obj = json.loads(j)
    for attr in [a for a in validtask.__dict__ if not a.startswith("_")]:
        assert attr in obj
