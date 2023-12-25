from django.shortcuts import render,redirect
from .forms import TaskForm
from .models import TaskModel

# Create your views here.
def add_task(request):
    if request.method=='POST':
        task_from=TaskForm(request.POST)
        if task_from.is_valid():
            task_from.save()
            return redirect('homepage')
    else:
        task_from=TaskForm()
    return render(request,'add_task.html',{'form':task_from})

def edit_task(request,id):
    taskform=TaskModel.objects.get(pk=id)
    task_from=TaskForm(instance=taskform)
    if request.method=='POST':
        task_from=TaskForm(request.POST,instance=taskform)
        if task_from.is_valid():
            task_from.save()
            return redirect('homepage')
    return render(request,'add_task.html',{'form':task_from})

def delete_task(request,id):
    taskform=TaskModel.objects.get(pk=id)
    taskform.delete()
    return redirect('homepage')