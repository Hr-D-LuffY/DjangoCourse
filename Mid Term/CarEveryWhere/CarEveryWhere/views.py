from django.shortcuts import render, redirect
from car.models import brand,car
from car.forms import CommentForm
from buyer.models import Buyer
from django.contrib import messages
from django.views.generic import DetailView
# Create your views here.
def homepage(request,brand_slug=None):
    allbrand= brand.objects.all()
    allcar=car.objects.all()
    if brand_slug is not None:
        category = brand.objects.get(name = brand_slug)
        allcar = car.objects.filter(brand  = category)
    return render(request,'home.html',{'brand':allbrand,'cars':allcar})

def buyCar(request,id):
    cardetail=car.objects.get(pk=id)
    buy=Buyer.create(request.user,cardetail)
    buy.save()
    carquantity = cardetail.quantity-1
    cardetail.quantity = carquantity
    cardetail.save()
    messages.success(request,'Buying Successfull')
    return redirect('profile')

class DetailPostView(DetailView):
    model = car
    pk_url_kwarg = 'id'
    template_name = 'cardetails.html'
    
    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object 
        comments = post.comments.all()
        comment_form = CommentForm()
        
        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
    