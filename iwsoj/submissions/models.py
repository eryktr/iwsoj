from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from tasks.models import Task
from .status import Status
from .language import Language


class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(choices=Status.choices(), default=Status.PENDING.value, max_length=12)
    sourceCode = models.TextField()
    language = models.CharField(choices=Language.choices(), max_length=8)
    createdate = models.DateTimeField(default=timezone.now)
