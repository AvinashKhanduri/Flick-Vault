from django.db import models
from base.models import baseModel
from home.models import *
from accounts.models import *
from payments.models import Payment

class Screen(baseModel):
    screen_number = models.IntegerField()
    total_seats = models.IntegerField()
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE,related_name="screens")

    class Meta:
        ordering = ['screen_number']  # Order by screen_number ascending
        verbose_name = "Screen"
        verbose_name_plural = "Screens"

    def __str__(self):
        return f"Theater: {self.theater.name}, Screen number: {self.screen_number}"
    
    
    
class Show(baseModel):
    show_time = models.TimeField()
    date = models.DateField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="shows")
    screen = models.ForeignKey(Screen,on_delete=models.CASCADE,related_name="shows")
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE,related_name="shows")
    
    # def __str__(self):
        # return f"show name {self.show_time}"
    


class Seat(baseModel):
    seat_number = models.IntegerField()
    PRIORITIES = (
    (0, 'Low'),
    (1, 'Normal'),
    (2, 'High'),
  )
    seat_type = models.IntegerField(default=1,choices=PRIORITIES)
    availability_status = models.BooleanField(default=True)
    screen = models.ForeignKey(Screen,on_delete=models.CASCADE,related_name="seats")



class Booking(baseModel):
    booking_date = models.DateField()
    total_price = models.IntegerField()
    payment_status = models.BooleanField(default=False)
    user = models.ForeignKey(profile, on_delete=models.CASCADE,related_name="bookings")
    show = models.ForeignKey(Show,on_delete=models.CASCADE,related_name="bookings")
    payment = models.OneToOneField(Payment,on_delete=models.CASCADE,related_name="bookings")

