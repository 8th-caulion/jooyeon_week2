from django.contrib import admin
from django.urls import path
import food.views
#from .import views

urlpatterns = [
    path('food/',food.views.food, name= "food"),
    path('food/<int:food_id>', food.views.detail, name = "detail"),
    path('food/new',food.views.new, name = "new"),
    path('food/create',food.views.create, name = "create"),
    path('food/edit/<int:food_id>', food.views.edit, name = "edit"),
    path('food/update/<int:food_id>', food.views.update, name = "update"),
    path('food/delete/<int:food_id>', food.views.delete, name = "delete"),
]