from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="Home"),
    path('contact', views.contact, name="Contact"),
    path('about', views.about, name="About"),
    # path('search', views.search, name='search'),
#     path('signup', views.handlesignup, name="Sign Up"),
#     path('login', views.handlelogin, name="Login"),
#     path('logout', views.handlelogout, name="Logout")
]