from django.shortcuts import render,redirect
from books.models import book, Bookcategory,Reviews
from account.models import account,borrower
from django.contrib import messages
from books.forms import ReviewForm
from django.core.mail import EmailMessage, EmailMultiAlternatives
from django.template.loader import render_to_string


def send_borrow_email(user,book, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'book' :book
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()
# Create your views here.
def home(request,brand_slug=None):
    allbooks=book.objects.all()
    allcatergories= Bookcategory.objects.all()
    if brand_slug is not None:
        category = Bookcategory.objects.get(name = brand_slug)
        allbooks = book.objects.filter(brand  = category)
    return render(request,'index.html',{'categories':allcatergories,'books':allbooks})

def bookdetails(request,id):
    book_detail= book.objects.get(id=id)
    bookreview=Reviews.objects.filter(post=book_detail)

    account_instance = account.objects.get(user=request.user)
    borrower_instance = borrower.objects.filter(borrower_name=account_instance)
    
    for i in borrower_instance:
            if i.books==book_detail:
                match=True
                break
            else:
                match=False
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            newReview=form.save(commit=False)
            newReview.post=book_detail
            newReview.save()
    else:
         form=ReviewForm()
    return render(request,'bookdetails.html',{'form':form,'book':book_detail,'Reviews':bookreview,'match':match})

def borrowBook(request, id):
    book_detail = book.objects.get(pk=id)
    account_instance = account.objects.get(user=request.user)
    if account_instance.amount >=book_detail.borrowing_price:
        borrower_instance = borrower(borrower_name=account_instance, books=book_detail)
        borrower_instance.save()

        account_instance.amount -= book_detail.borrowing_price
        account_instance.save()

        
        send_borrow_email(request.user,book_detail,"Borrowing Book Message", "borrowbookEmail.html")  
        messages.success(request, 'Borrowing Successful')
    else:
        messages.warning(request, 'You have less amount then borrowing price!')
    return redirect('profile')

def returnBook(request, id):
    book_detail = book.objects.get(pk=id)
    account_instance = account.objects.get(user=request.user)
    borrower_instance = borrower.objects.get(borrower_name=account_instance, books=book_detail)
    
    borrower_instance.delete()

    account_instance.amount += book_detail.borrowing_price
    account_instance.save()
    messages.success(request, 'Successfully Return the Book')
    return redirect('profile')

