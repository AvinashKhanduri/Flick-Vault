from django.shortcuts import render,redirect
from home.models import *
from booking.models import *
from django.http import Http404
from base.utils import isAvaliable
import random
import datetime
from payments.models import *
from base.emails import send_ticket_booking_email
from django.contrib.auth.decorators import login_required


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

@login_required(redirect_field_name="login")
def selectSeat(request, show_id):
    try:
        # Get the show instance based on the provided show_id
        show = Show.objects.get(uid=show_id)

        ticket_count = 0
        total_amount = 0.0

        # Check if the request method is POST and the necessary fields are provided
        if request.method == 'POST':
            ticket_count = int(request.POST.get('ticket_count', 0))  # Default to 0 if not provided
            total_amount = float(request.POST.get('total_amount', 0.0))  # Default to 0 if not provided

            # Additional validation: check if ticket count and total amount are positive
            if ticket_count <= 0 or total_amount <= 0:
                # You can handle errors here, such as displaying a message to the user
                return render(request, "booking/seatSelection.html", {
                    "show": show,
                    "error": "Invalid ticket count or amount."
                })
            payment = Payment(amount = total_amount,payment_date = datetime.datetime.now().date(),payment_method = "Dummy Payment")
            payment.save()
            
            # Create the booking object and save it to the database
            booking = Booking(total_price=total_amount, user=request.user.profile, show=show, payment = payment)
            booking.save()

            ticket = Ticket(booking = booking,screen = show.screen,total_person = ticket_count)
            ticket.save()

            send_ticket_booking_email(username=request.user.first_name,movie=show.movie.title,theater=show.theater.name,address=show.theater.location,date=show.date,number_of_tickets=ticket_count,total_price=total_amount,email=request.user.email)

            # Optionally, you could pass the booking instance to the template to show a confirmation
            return redirect('thankyou')

        # If it's not a POST request, just render the page with the show data
        return render(request, "booking/seatSelection.html", {
            "show": show,
        })

    except Show.DoesNotExist:
        raise Http404("Show not found.")


def thankyou(request):
    return render(request, "booking/thankyou.html")

def myBooking(request):
    if request.user.is_authenticated:
        try:
            bookings = Booking.objects.filter(user=request.user.profile)
            return render(request,"booking/mybooking.html",context={"bookings":bookings})
        except Exception as e:
            bookings = None
            return render(request,"booking/mybooking.html",context={"bookings":bookings})
    else:
        return redirect("login")
