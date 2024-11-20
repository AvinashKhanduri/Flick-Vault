from django.shortcuts import render
from home.models import *
# Create your views here.
def movieDetailPage(request, movie_id):
    try:
        movie = Movie.objects.get(uid=movie_id) 
        return render(request, 'booking/movieDetail.html', context={"movie": movie})
    except Movie.DoesNotExist:
        return render(request, '404.html')  
    

def bookingPage(request):
    theater = Theater.objects.all()
    city = set()
    for i in theater:
        city.add(i.city)

    return render(request,"booking/bookingPage.html" ,context={"cities":city})

def selectCity(request, city):
    try:
        theater = Theater.objects.get(city=city)
        return render(request,"booking/bookingPage.html", content_type={"theaters":theater})
    except Exception as e:
        return render(render,"404.html")

