from django.http import HttpResponse

def home(request):
    return HttpResponse("THIS IS HOME")

def contact(request):
    return HttpResponse("THIS IS CONTACT ")