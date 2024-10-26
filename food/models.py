from django.db import models
from base.models import baseModel
from booking.models import Booking

# Create your models here.
class FoodItem(baseModel):
        name = models.CharField(max_length=70)
        description = models.TextField(null=False,blank=False)
        price =models.IntegerField(blank=False)   
        FOOD_CHOICES = (
            ("GUJARATI", 'Gujarati'),
            ("SOUTH INDIAN", 'South Indian'),
            ('KASHMIRI', 'Kashmiri'),
            ("MALVANI","Malvani")
            )
     
        catagory = models.CharField(max_length=50,choices=FOOD_CHOICES)

        def __str__(self):
                return self.name
        

class FoodOrder(baseModel):
        booking_id = models.ForeignKey(Booking,on_delete=models.CASCADE,related_name="foodOrders")
        total_price = models.IntegerField(blank=False)
        order_date = models.DateField()
        PAYMENT_STATUS_CHOICES = (
                (0,"pending"),
                (2,"complete"),
                (3,"failed")
        )
        payment_status = models.CharField(max_length=20,choices=PAYMENT_STATUS_CHOICES)

        def __str__(self):
                pass


class OrderItem(baseModel):
        food_order_id = models.ForeignKey(FoodOrder,on_delete=models.CASCADE,related_name="orderItems")
        foo_order_item = models.ForeignKey(FoodItem,on_delete=models.CASCADE,related_name="orderItems")
        quantity = models.IntegerField()
        item_Price = models.IntegerField()
        