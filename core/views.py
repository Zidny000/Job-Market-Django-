from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth import authenticate, logout
from django.http import HttpResponseRedirect

from .models import Category,Post

from .forms import SignupForm
# Create your views here.

def UserLoggedIn(request):
    if request.user.is_authenticated == True:
        username = request.user.username
    else:
        username = None
    return username

def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    return render(request,'core/index.html',{
        'posts' : posts,
        'categories' : categories
    })

def login(request):
    username = UserLoggedIn(request)
    if username != None:
        return redirect('/')
    else :
        return render(request,'core/login.html')

def logout_view(request):
    username = UserLoggedIn(request)
    if username != None:
        logout(request)
        return redirect('/')
    else :
        return redirect('/')


def signup(request):

    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
       
            return redirect('/login/')
            
        else:
            context = {
                'form':form
                }
            return render(request, 'core/signup.html', context)
    form = SignupForm()
    context = {
            'form':form
        }
    return render(request, 'core/signup.html', context)


def jobpost(request):
    return render(request,'core/jobpost.html')

def profile(request):
    username = UserLoggedIn(request)
    if username != None:
        
        return render(request,'core/profile.html')
    else :
        return redirect('/')

def jobdetails(request,pk):
    job = get_object_or_404(Post,pk=pk)
    related_jobs = Post.objects.filter(category=job.category).exclude(pk=pk)[0:3]
    return render(request,'core/jobdetails.html',{
        'job':job,
        'related_items':related_jobs
    })
