
from django.contrib import admin
from .models import BlogPost

# Register your models here.
@admin.register(BlogPost)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['sno', 'title', 'author', 'content']