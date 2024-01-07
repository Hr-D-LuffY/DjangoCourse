from django.shortcuts import render,redirect
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm 
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse
from account.models import account,borrower

from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string


def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()
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
    form_class= forms.LoginForm
    template_name='login.html'
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
    acc=account.objects.filter(user= request.user)
    account_instance = account.objects.get(user=request.user)
    borrowingList= borrower.objects.filter(borrower_name=account_instance)
    print(account_instance.user.username)
    if len(acc)==0:
        newaccount=account(user= request.user)
        newaccount.save()
    useraccount=account.objects.get(user= request.user)
    return render(request, 'profile.html',{'acc':account_instance,'lists':borrowingList})


class userLogout(LogoutView):
    def get(self, request):
        logout(request)
        messages.success(request,"Logged out Succesfully")
        return redirect('homepage')

@login_required
def deposite(request):
    if request.method == 'POST':
        form = forms.DepositForm(data=request.POST)
        if form.is_valid():
            amount=form.cleaned_data['amount']
            acc=account.objects.get(user=request.user)
            acc.amount+=amount
            acc.save()
            
            messages.success(request,"Deposite Succesfully")
            send_transaction_email(request.user, amount, "Deposite Message", "deposite_email.html")
            return redirect('profile')
    else:
        form =forms.DepositForm()

    return render(request, 'deposite.html', {'form': form})