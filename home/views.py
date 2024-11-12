from django.shortcuts import render
from home.models import *

# Create your views here.

def landingPage(request):
    return render(request, 'home/landingPage.html')

def homepage(request):
    movieData = Movie.objects.all()
    

    return render(request,'home/home.html')
