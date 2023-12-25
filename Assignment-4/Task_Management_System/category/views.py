from django.shortcuts import render
from .forms import TaskCategoryForm

# Create your views here.
def add_category(request):
    if request.method=='POST':
        cate_form=TaskCategoryForm(request.POST)
        if cate_form.is_valid():
            cate_form.save()
    else:
        cate_form=TaskCategoryForm()
    return render(request,'add_category.html',{'form':cate_form})
