from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data) -> Task:
        task = Task.objects.create(
            title=validated_data['title'],
            statement=validated_data['statement'],
            complexity=validated_data['complexity'],
            definition=validated_data['definition'],
        )
        return task
