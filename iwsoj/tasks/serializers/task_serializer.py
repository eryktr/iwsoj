from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"
        extra_kwargs = {
            'input_public': {'write_only': True},
            'output_public': {'write_only': True},
            'input_hidden': {'write_only': True},
            'output_hidden': {'write_only': True}
        }

    def create(self, validated_data) -> Task:
        """
        :param validated_data: validated field of the task (title, statement, complexity, input, output)
        
        :return: model of the task
        """
        task = Task.objects.create(
            title=validated_data['title'],
            statement=validated_data['statement'],
            complexity=validated_data['complexity'],
            input_public=validated_data['input_public'],
            output_public=validated_data['output_public'],
            input_hidden=validated_data['input_hidden'],
            output_hidden=validated_data['output_hidden']
        )
        return task
