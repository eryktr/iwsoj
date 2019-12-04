from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"

    def create(self, validated_data) -> Task:
        """
        :param validated_data: validated field of the task (title, statement, complexity, input, output)
        
        :return: model of the task
        """
        task = Task.objects.create(
            title=validated_data['title'],
            statement=validated_data['statement'],
            complexity=validated_data['complexity'],
            input=validated_data['input'],
            output=validated_data['output']
        )
        return task
