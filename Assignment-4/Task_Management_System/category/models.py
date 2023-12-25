from django.db import models
# Create your models here.
class TaskCategory(models.Model):
    CategoryName= models.CharField(max_length=50)

    def __str__(self):
        return self.CategoryName
    
