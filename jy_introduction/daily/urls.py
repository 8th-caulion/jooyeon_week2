from django.contrib import admin
from django.urls import path
import daily.views
#from .import views

urlpatterns = [
    path('daily/',daily.views.travel, name= "travel"),
    path('food/',daily.views.food, name= "food"),
]