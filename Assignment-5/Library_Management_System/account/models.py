from django.db import models
from django.contrib.auth.models import User
from books.models import book
# Create your models here.
class account(models.Model):
    user= models.OneToOneField(User,on_delete= models.CASCADE )
    amount = models.IntegerField(default=0)


    def __str__(self):
        return self.user.username
    
class borrower(models.Model):
    borrower_name= models.ForeignKey(account,on_delete= models.CASCADE)
    books=models.ForeignKey(book,on_delete= models.CASCADE)
    borrowed_on = models.DateTimeField(auto_now_add=True)

    