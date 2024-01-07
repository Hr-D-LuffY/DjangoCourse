from django.db import models

# Create your models here.
class Bookcategory(models.Model):
    name= models.CharField(max_length=30)

    def __str__(self):
        return self.name
    

class book(models.Model):
    title= models.CharField(max_length=50)
    borrowing_price = models.IntegerField()
    description= models.TextField()
    brand = models.ForeignKey(Bookcategory, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='static/uploads/')


    def __str__(self):
        return self.title
    
class Reviews(models.Model):
    post = models.ForeignKey(book, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=30)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True) # jkhn e ei class er object toiri hobe sei time ta rekhe dibe
    
    def __str__(self):
        return f"Comments by {self.name}"