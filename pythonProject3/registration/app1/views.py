from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return render(request, 'home.html')
    # return HttpResponse('Hello world')
def login_view(request):
    return render(request, 'login.html',{'signup':'soon'})

def signup_view(request):
    return render(request, 'signup.html',{'signup':'soon'})