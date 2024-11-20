from django.shortcuts import render
from home.models import *
from booking.models import *
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
    theaters = Theater.objects.filter(city=city).prefetch_related('shows')  # Prefetch shows for each theater
    theater = Theater.objects.all()
    city = set()
    for i in theater:
        city.add(i.city)

    if theaters.exists():  # Check if theaters exist
        return render(request, "booking/bookingPage.html", context={"theaters": theaters,"cities":city})
    else:
        return render(request, "404.html")  # Show 404 if no theaters found


