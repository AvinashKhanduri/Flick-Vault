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
    

def bookingPage(request, movie_id):
    try:
        movie = Movie.objects.get(uid=movie_id)
        theater = Theater.objects.all()
        city = {i.city for i in theater}  # Using set comprehension for cleaner code

        return render(request, "booking/bookingPage.html", context={"cities": city, "movie": movie})
    except Movie.DoesNotExist:
        return render(request, "404.html")  # Or use Http404


def selectCity(request, city, movie_id):
    try:
        movie = Movie.objects.get(uid=movie_id)  # Get the movie object by movie_id
        theater = Theater.objects.all()
        shows = Show.objects.filter(theater__city=city, movie__uid = movie_id)
        cities = {i.city for i in theater}  # Using set comprehension for cleaner code

        if shows.exists():
            return render(request, "booking/bookingPage.html", context={
                "shows": shows,  # Pass the shows related to the selected city
                "cities": cities,  # Pass the set of cities
                "movie": movie,  # Pass the movie object to display movie details
            })
        else:
            movie = Movie.objects.get(uid=movie_id)  # Get the movie object by movie_id
            theater = Theater.objects.all()
            shows = Show.objects.filter(theater__city=city, movie__uid = movie_id)
            cities = {i.city for i in theater}  # Using set comprehension for cleaner code
            return render(request, "booking/bookingPage.html", context={
                "shows": shows,  # Pass the shows related to the selected city
                "cities": cities,  # Pass the set of cities
                "movie": movie,  # Pass the movie object to display movie details
            })
    except Movie.DoesNotExist:
        return render(request, "404.html")  # Handle case when movie does not exist

def selectSeat(request, show_id):
    show = Show.objects.get(uid = show_id)
    screen = show.screen
    seats = Seat.objects.filter(screen=screen)

    return render(request, "booking/seatSelection.html",context={"show":show,"seats":seats})



