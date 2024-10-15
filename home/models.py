from django.db import models
from base.models import baseModel


class Movie(baseModel):
    title = models.TextField(max_length=100)
    genre = models.TextField(max_length=100)
    duration = models.IntegerField()
    language = models.TextField(max_length=100)
    PRIORITIES = (
    (0, '0 star'),
    (1, '1 Star'),
    (2, '2 Star'),
    (3, '3 Star'),
    (4, '4 Star'),
    (5, '5 Star')
  )
    rating = models.IntegerField(default=0,choices=PRIORITIES)
    release_date = models.DateField()

    def __str__(self)->str:
        return self.title
    

class Theater(baseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    total_screens = models.IntegerField()

    def __str__(self):
        return self.name
    
