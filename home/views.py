from django.shortcuts import render

# Create your views here.

def landingPage(request):
    return render(request, 'home/landingPage.html')

def homepage(request):
    return render(request,'home/home.html')
