
from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['sno', 'title', 'author', 'content']


@admin.register(Comments)
class BlogcommentAdmin(admin.ModelAdmin):
    list_display = ['sno', 'comment', 'user', 'post', 'parent']