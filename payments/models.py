from django.db import models
from  base.models import baseModel

class Payment(baseModel):
    amount = models.IntegerField()
    payment_date = models.DateField()
    payment_method = models.TextField()

class Ticket(baseModel):
    qr_code = models.ImageField(upload_to="ticket_qr_Codes")
    