from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("bookticket/",bookingPage,name="bookingpage"),
    path("movie/<movie_id>/",movieDetailPage,name="movieDetailPage"),
    path("city/<city>/",selectCity,name="seleccity")
    
    
] 
