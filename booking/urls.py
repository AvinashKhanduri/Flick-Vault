from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("bookticket/<movie_id>",bookingPage,name="bookingpage"),
    path("movie/<movie_id>/",movieDetailPage,name="movieDetailPage"),
    path("city/<city>/<movie_id>/", selectCity, name="selectcity"),  # Modified to include both city and movie_id
    path("bookSeat/<show_id>/", selectSeat,name="selectSeat"),
] 
