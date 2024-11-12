from django.db import models
from base.models import baseModel


class Movie(baseModel):
    title = models.TextField(max_length=100)
    region = models.CharField(max_length=20)
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
    

class MoviePoster(baseModel):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='posters')
  poster = models.ImageField(upload_to='posters')

  def __str__(self):
      return f"Movie {self.movie.title}"
  


class Theater(baseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    total_screens = models.IntegerField()

    def __str__(self):
        return self.name
    
