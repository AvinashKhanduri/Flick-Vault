from django.contrib import admin
from booking.models import *

# Register your models here.
# admin.site.register([Show,Seat,Booking])

class ScreenInline(admin.TabularInline):
    model = Screen
    extra = 0  # Number of empty forms to display

class TheaterAdmin(admin.ModelAdmin):
    list_display = ('name',)  # Show theater name in the admin list
    inlines = [ScreenInline]  # Inline screens in the theater admin view

class ScreenAdmin(admin.ModelAdmin):
    list_display = ('theater', 'screen_number', 'total_seats')  # Display theater name and screen details
    list_filter = ('theater',)  # Filter by theater
    ordering = ('theater', 'screen_number')  # Order by theater and screen number

# Register your models with the admin site
admin.site.register(Theater, TheaterAdmin)
admin.site.register(Screen, ScreenAdmin)
