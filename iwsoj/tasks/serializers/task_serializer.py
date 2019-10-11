from rest_framework import serializers

from tasks.models import Task


class TaskSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Task
        fields = "__all__"

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass
