from django.db import models
from django.contrib.auth.models import User
from car.models import car
# Create your models here.
class Buyer(models.Model):
    buyer_name = models.ForeignKey(User,on_delete= models.CASCADE , unique = False)
    cars = models.ForeignKey(car, on_delete=models.CASCADE)

    @classmethod
    def create(cls, name , cars):
        obj = cls(buyer_name=name,cars=cars)
        return obj
    
    def __str__(self):
        return f'{self.buyer_name}-{self.cars}'
    