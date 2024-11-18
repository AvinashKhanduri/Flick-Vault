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
    return render(request,"booking/bookingPage.html")

