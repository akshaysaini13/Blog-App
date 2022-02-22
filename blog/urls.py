from django.db import models

# Create your models here.
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("",views.home)
]