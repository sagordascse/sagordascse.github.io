from django.http import HttpResponse
from django.shortcuts import render
from .models import BlogPost

def index(request):
    myPosts=BlogPost.objects.all()
    return render(request,"blog/index.html",{'myPosts':myPosts})

def blogPost(request, id):
    post = BlogPost.objects.filter(post_id = id)[0]
    return render(request, 'blog/blogPost.html',{'post':post})