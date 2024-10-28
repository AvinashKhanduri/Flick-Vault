from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path("login/", loginPage,name="login"),
    path("register/",RegisterPage,name="register"),
    path("activate/<email_token>",activate_account)
] 
