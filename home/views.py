from django.db.models import query
from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# from blog.models import Post
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# Create your views here.

# HTML Pages
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        content = request.POST.get('content')

        if len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4:
            messages.error(request, "Please fill the form correctly!")
        else: 
            con = Contact(name=name, email=email, phone=phone, content=content)
            con.save()
            messages.success(request, "Submitted Successfully! We will get back to you shortly")

    return render(request, 'home/contact.html')


# def search(request):
#     mysearch = request.GET['search']
#     if len(mysearch) > 68:
#         allPosts = Post.objects.none()
#     else:
#     # allPosts = Post.objects.all()
#         allPostsTitle = Post.objects.filter(title__icontains=mysearch)
#         allPostContent = Post.objects.filter(content__icontains=mysearch)
#         allPosts = allPostsTitle.union(allPostContent)
#     if allPosts.count == 0:
#         messages.error(request, "No Search results found!")
#     params = {'allPosts': allPosts, 'query': mysearch}
#     return render(request, 'home/search.html', params)

# Authentication APIs
def handlesignup(request):
    #Creating new user
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if len(username) > 10: # length should be greater than 10
            messages.error(request, "Username must be under 10 characters")
            return redirect('/')

        if not username.isalnum(): # should be alphanumeric
            messages.error(request, "Username can only contain letters and numbers")
            return redirect('/')

        if password1 != password2:
            messages.error(request, "Password does not match. Try again")
            return redirect('/')

        else: 
            user = User.objects.create_user(username, email, password1)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            messages.success(request, "Account has been successfully created!")
            return redirect('/')
    else:
        return HttpResponse('404 - Page not found')   
    

def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST.get('loginusername')
        loginpassword = request.POST.get('loginpassword')

        user = authenticate(username=loginusername, password=loginpassword)
        # print(user)
        
        if user is not None:
            login(request, user)
            messages.success(request," Successfully logged in!")
            return redirect("/")
            
        else:
            messages.error(request, "Invalid credentials. Please try again!")
            return redirect("/")
    return HttpResponse('404 - Page not found') 


def handlelogout(request):
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('/')