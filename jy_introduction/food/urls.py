from django.contrib import admin
from django.urls import path
import food.views
#from .import views

urlpatterns = [
    path('food/',food.views.food, name= "food"),
    path('food/<int:food_id>', food.views.detail, name = "food_detail"),
    path('food/new',food.views.new, name = "food_new"),
    path('food/create',food.views.create, name = "food_create"),
    path('food/edit/<int:food_id>', food.views.edit, name = "food_edit"),
    path('food/update/<int:food_id>', food.views.update, name = "food_update"),
    path('food/delete/<int:food_id>', food.views.delete, name = "food_delete"),
]