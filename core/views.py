from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'core/index.html')

def login(request):
    return render(request,'core/login.html')

def signup(request):
    return render(request,'core/signup.html')

def jobpost(request):
    return render(request,'core/jobpost.html')

def profile(request):
    return render(request,'core/profile.html')

def jobdetails(request):
    return render(request,'core/jobdetails.html')
