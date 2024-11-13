from django.shortcuts import render
from home.models import *

# Create your views here.

def landingPage(request):
    return render(request, 'home/landingPage.html')

def homepage(request):
    movieData = Movie.objects.all()[:10]
    recommended = Movie.objects.all()[10:20]
    return render(request,'home/home.html',context={"movieData":movieData,"recommended":recommended})
