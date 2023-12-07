from django.db import models
from category.models import Task

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    tasks = models.ManyToManyField(Task)