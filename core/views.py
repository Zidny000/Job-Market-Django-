from django.shortcuts import render,get_object_or_404

from .models import Category,Post


# Create your views here.

def index(request):
    categories = Category.objects.all()
    posts = Post.objects.all()
    # development_posts = Post.objects.filter(category=categories[1].pk)[0:3]
    # bank_posts = Post.objects.filter(category=categories[0].pk)[0:3]
    return render(request,'core/index.html',{
        'posts' : posts,
        # 'development_posts': development_posts,
        # 'bank_posts' : bank_posts,
        'categories' : categories
    })

def login(request):
    return render(request,'core/login.html')

def signup(request):
    return render(request,'core/signup.html')

def jobpost(request):
    return render(request,'core/jobpost.html')

def profile(request):
    return render(request,'core/profile.html')

def jobdetails(request,pk):
    job = get_object_or_404(Post,pk=pk)
    related_jobs = Post.objects.filter(category=job.category).exclude(pk=pk)[0:3]
    return render(request,'core/jobdetails.html',{
        'job':job,
        'related_items':related_items
    })
