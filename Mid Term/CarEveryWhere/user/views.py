from django.shortcuts import render,redirect
from . import forms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login ,logout
from buyer.models import Buyer
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse

# Create your views here.
def signup(request):
    if request.method=='POST':
        signupform= forms.Registration(request.POST)
        if signupform.is_valid():
            signupform.save()
            messages.success(request,'Account Created Succesfully')
            return redirect('user_login')
    else:
        signupform=forms.Registration()
    return render(request, 'signup.html',{'form': signupform, 'type':'Signup'})


class user_Login(LoginView):
    form_class= AuthenticationForm
    template_name='signup.html'
    def get_success_url(self):
        return reverse('profile')

    def post(self, request, *args, **kwargs):
  
        form = self.get_form()
        if form.is_valid():
            messages.success(request,"Logged in Succesfully")
            return self.form_valid(form)
        else:
            messages.warning(request,"Logged Information Incorrect!!")
            return self.form_invalid(form)

@login_required
def profile(request):
    carlist= Buyer.objects.filter(buyer_name= request.user)
    print(carlist)
    return render(request, 'profile.html',{'cars':carlist})


class userLogout(LogoutView):
    def get(self, request):
        logout(request)
        messages.success(request,"Logged out Succesfully")
        return redirect('homepage')

@login_required
def edit_profile(request):
    if request.method=='POST':
        userchange= forms.ChangeuserForm(request.POST, instance=request.user)
        if userchange.is_valid():
            userchange.save()
            messages.success(request,'Account Updated Succesfully')
            return redirect('profile')
    else:
        userchange=forms.ChangeuserForm(instance=request.user)
    return render(request, 'updateprofile.html',{'form': userchange})
