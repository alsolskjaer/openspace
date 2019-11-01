from django.db import models


class ToDo(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    due_date = models.DateTimeField()
    user = models.CharField(max_length=64)
    isDone = models.BooleanField(default=False)

class Cafe(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    available_seat = models.IntegerField()

