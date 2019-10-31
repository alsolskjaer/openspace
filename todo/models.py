from django.db import models


class ToDo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    user = models.CharField(max_length=64)
    isDone = models.BooleanField(default=False)
