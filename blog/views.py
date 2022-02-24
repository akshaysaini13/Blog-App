from turtle import pos
from .models import BlogPost, Comments
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from blog.templatetags import get_dict

# Create your views here.

def home(request):   
    if request.method == 'GET':
        post = BlogPost.objects.all()
        post = {'allPosts': post}
    return render(request, 'blog/blogHome.html', post)


def viewBlog(request, sno):
    if request.method == 'GET':
        blog = BlogPost.objects.filter(sno=sno).first()
        postcomments = Comments.objects.filter(post=sno, parent=None)
        replies = Comments.objects.filter(post=sno).exclude(parent=None)
        replyDict = {}
        for reply in replies:
            if reply.parent.sno not in replyDict.keys():
                replyDict[reply.parent.sno] = [reply]
            else:
                replyDict[reply.parent.sno].append(reply)

        print(postcomments, replies)
        print(replyDict)
        view_blog = {'post': blog, 'comment': postcomments, 'user':request.user, 'replyDict':replyDict}

    return render(request, 'blog/blogPost.html', view_blog)


def post_comment(request):
    if request.method == 'POST':
        comment = request.POST.get('comment')
        user = request.user
        postid =  request.POST.get('postid')
        post = BlogPost.objects.get(sno=postid)
        parentsno = request.POST.get('parentsno')
        if parentsno == "":
            comment = Comments(comment=comment,user=user, post=post)
        else:
            parent = Comments.objects.get(sno=parentsno)
            comment = Comments(comment=comment,user=user, post=post, parent=parent)
        comment.save()
        messages.success(request, "Reply posted successfully!")

    return redirect(f'/blog/{post.sno}')
