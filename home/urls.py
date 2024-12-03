from django.contrib import admin
from django.urls import path,include
from .views import *


urlpatterns = [
   path('',landingPage,name="dummy"),
   path('home/',homepage,name="homePage"),
   path('About/',AboutUs,name="about"),
   path('ContactUs/',ContactUs,name="contact"),
] 