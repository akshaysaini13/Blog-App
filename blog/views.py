from .models import BlogPost
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def home(request):
    
    if request.method == 'GET':
        post = BlogPost.objects.all()
        print(post)

        post = {'allPosts': post}

    return render(request, 'blog/blogHome.html', post)


def viewBlog(request, sno):
    if request.method == 'GET':
        blog = BlogPost.objects.get(sno=sno)
        print(blog)
        
        view_blog = {'post': blog}

    return render(request, 'blog/blogPost.html', view_blog)
    