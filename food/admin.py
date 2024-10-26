from django.contrib import admin
from food.models import *
# Register your models here.

admin.site.register([FoodItem,FoodOrder,OrderItem])

