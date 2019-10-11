from django.db import models
from django.utils import timezone
from django_mysql.forms import JSONField

from tasks.complexity import Complexity


class Task(models.Model):
    title = models.CharField(max_length=255, unique=True)
    statement = models.TextField()
    createdate = models.DateTimeField(default=timezone.now)
    complexity = models.IntegerField(choices=Complexity.choices())
    definition = JSONField()
