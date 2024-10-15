from django.db import models
from base.models import baseModel
from home.models import *
from accounts.models import *

class Screen(baseModel):
    screen_number = models.IntegerField()
    total_seats = models.IntegerField()
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE,related_name="theater")

    def __str__(self):
        return f"screen number {self.screen_number}"
    
class Show(baseModel):
    show_time = models.TimeField()
    date = models.DateField()
    movie = models.ForeignKey(Movie,on_delete=models.CASCADE,related_name="show")
    screen = models.ForeignKey(Screen,on_delete=models.CASCADE,related_name="show")
    theater = models.ForeignKey(Theater,on_delete=models.CASCADE,related_name="show")
    
    def __str__(self):
        return f"show name {self.show_time}"
    


class Seat(baseModel):
    seat_number = models.IntegerField()
    PRIORITIES = (
    (0, 'Low'),
    (1, 'Normal'),
    (2, 'High'),
  )
    seat_type = models.IntegerField(default=1,choices=PRIORITIES)
    availability_status = models.BooleanField(default=True)
    screen = models.ForeignKey(Screen,on_delete=models.CASCADE,related_name="screen")


class Booking(baseModel):
    booking_date = models.DateField()
    total_price = models.IntegerField()
    payment_status = models.BooleanField(default=False)
    user = models.ForeignKey(profile, on_delete=models.CASCADE,related_name="profile")