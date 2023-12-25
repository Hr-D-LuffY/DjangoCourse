from django.db import models
from category.models import TaskCategory

# Create your models here.
class TaskModel(models.Model):
    taskTitle= models.CharField(max_length=50)
    taskDescription= models.TextField(max_length=100)
    category= models.ManyToManyField(TaskCategory)
    is_completed= models.BooleanField()
    assignDate= models.DateField()
    

    def __str__(self):
        return self.taskTitle