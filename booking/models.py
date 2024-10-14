from django.db import models
from base.models import baseModel

class Screen(baseModel):
    screen_number = models.IntegerField()
    total_seats = models.IntegerField()

    def __str__(self):
        return f"screen number {self.screen_number}"
    
class Show(baseModel):
    show_time = models.TimeField()
    date = models.DateField()
    
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


class Booking(baseModel):
    booking_date = models.DateField()
    total_price = models.IntegerField()
    payment_status = models.BooleanField(default=False)
    