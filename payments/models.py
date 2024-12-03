from django.db import models
from  base.models import baseModel
import datetime


class Payment(baseModel):
    amount = models.IntegerField()
    payment_date = models.DateField()
    payment_method = models.TextField()



class Ticket(baseModel):
    # qr_code = models.ImageField(upload_to="ticket_qr_Codes")
    booking = models.OneToOneField('booking.Booking',on_delete=models.CASCADE,related_name="ticket")
    screen = models.ForeignKey('booking.Screen',on_delete=models.CASCADE,related_name="ticket")
    total_person = models.IntegerField(default=1)

    def __str__(self):
        return f"Ticket for booking id {self.booking.uid}"