from django.shortcuts import render
from task.models import TaskModel
from category.models import TaskCategory
# Create your views here.

def homepage(request):
    task=TaskModel.objects.all()
    
    return render(request,'home.html',{'task':task})