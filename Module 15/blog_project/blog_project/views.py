from django.shortcuts import render , redirect
from post.models import Post
# Create your views here.
def home(request):
    data=Post.objects.all()
    print(data)
    return render(request,'home.html',{'post':data})