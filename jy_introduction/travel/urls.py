from django.contrib import admin
from django.urls import path
import travel.views
#from .import views

urlpatterns = [
    path('travel/',travel.views.travel, name= "travel"),
    path('travel/<int:travel_id>', travel.views.detail, name = "travel_detail"),
    path('travel/new',travel.views.new, name = "travek_new"),
    path('travel/create',travel.views.create, name = "travel_create"),
    path('travel/edit/<int:travel_id>', travel.views.edit, name = "travel_edit"),
    path('travel/update/<int:travel_id>', travel.views.update, name = "travel_update"),
    path('travel/delete/<int:travel_id>', travel.views.delete, name = "travel_delete"),
]