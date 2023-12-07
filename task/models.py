from django.db import models

# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    isCompleted = models.BooleanField(default=False)
    date = models.DateField()