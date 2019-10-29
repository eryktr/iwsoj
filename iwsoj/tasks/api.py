from tasks.models import Task
from rest_framework import viewsets, permissions
from .serializers.task_serializer import TaskSerializer
from users.api import AuthUserToken


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    authentication_classes = [
        AuthUserToken
    ]
    permission_classes = [
        permissions.IsAuthenticated
    ]
    serializer_class = TaskSerializer
