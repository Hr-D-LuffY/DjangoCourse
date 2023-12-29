from django.shortcuts import render , redirect
from post.models import Post
from category.models import Category
# Create your views here.
def home(request,category_slug=None):
    data=Post.objects.all()
    if category_slug is not None:
        category=Category.objects.get(slug=category_slug)
        data= Post.objects.filter(category=category)
    categores=Category.objects.all()
    return render(request,'home.html',{'post':data, 'categories':categores})

# def category_wise_post(request,category_slug=None):
#     data=Post.objects.all()
#     categores=Category.objects.all()

#     if category_slug is not None:
#         category=category_slug
#         data= Post.objects.filter(category=category)
#     print(data)
#     return render(request,'home.html',{'post':data})