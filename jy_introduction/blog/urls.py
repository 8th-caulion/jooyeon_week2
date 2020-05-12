from django.contrib import admin
from django.urls import path
import blog.views
#from .import views

urlpatterns = [
    path('', blog.views.home, name = "home"), 
    path('profile/', blog.views.profile, name = "profile"),
]
