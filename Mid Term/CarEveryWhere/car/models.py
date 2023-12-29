from django.db import models

# Create your models here.
class brand(models.Model):
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class car(models.Model):
    car_model= models.CharField(max_length=50)
    price = models.IntegerField()
    quantity= models.IntegerField()
    description= models.TextField()
    brand = models.ForeignKey(brand, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='static/uploads/')


    def __str__(self):
        return self.car_model
    
class Comment(models.Model):
    post = models.ForeignKey(car, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # jkhn e ei class er object toiri hobe sei time ta rekhe dibe
    
    def __str__(self):
        return f"Comments by {self.name}"