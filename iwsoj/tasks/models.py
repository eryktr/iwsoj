from django.db import models
from django.utils import timezone

from tasks.complexity import Complexity


class Task(models.Model):
    title = models.CharField(max_length=255, unique=True)
    statement = models.TextField()
    createdate = models.DateTimeField(default=timezone.now)
    complexity = models.IntegerField(choices=Complexity.choices())
    input_public = models.TextField()
    output_public = models.TextField()
    input_hidden = models.TextField()
    output_hidden = models.TextField()
