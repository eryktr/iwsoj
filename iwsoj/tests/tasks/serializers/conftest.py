import pytest

from tasks.serializers.task_serializer import TaskSerializer


@pytest.fixture()
def validserializer(validtask):
    return TaskSerializer(validtask)
