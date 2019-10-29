from django.db import models
from django.utils import timezone

from tasks.complexity import Complexity


class Task(models.Model):
    title = models.CharField(max_length=255, unique=True)
    statement = models.TextField()
    createdate = models.DateTimeField(default=timezone.now)
    complexity = models.IntegerField(choices=Complexity.choices())
    input = models.TextField()
    output = models.TextField()
