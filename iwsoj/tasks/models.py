from django.db import models


class Task(models.Model):
    title = models.CharField(max_length=255)
    statement = models.TextField()
    createdate = models.DateTimeField(auto_now_add=True)
    #complexity = models.
