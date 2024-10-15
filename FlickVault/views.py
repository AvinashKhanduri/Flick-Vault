from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dummyView(request):
    return HttpResponse("This is for test only")