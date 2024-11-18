from django.db import models
from base.models import baseModel


class Movie(baseModel):
    title = models.TextField(max_length=100)
    region = models.CharField(max_length=20)
    genre = models.TextField(max_length=100)
    duration = models.IntegerField()
    language = models.TextField(max_length=100)
    sort_Description =models.TextField(max_length=50,default="Movies have always been a something good and better random text")
    long_Description = models.TextField(default="Movies have always been a captivating medium for storytelling, transporting audiences to fantastical worlds, unraveling gripping mysteries, and exploring the depths of human emotion. From the golden age of cinema to the modern era of CGI-laden blockbusters, the art of filmmaking has evolved tremendously, leaving an indelible mark on cultures worldwide.")
    
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
    

class MovieCast(baseModel):
    movie = models.ForeignKey(Movie,related_name="cast",on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    age = models.IntegerField(blank=True,null=True)
    about = models.TextField(blank=True,null=True)
    profilePhoto = models.ImageField(upload_to="castImages")

    def __str__(self) -> str:
        return f"{self.name} in {self.movie.title}"


class MoviePoster(baseModel):
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='posters')
  poster = models.ImageField(upload_to='posters')

  def __str__(self):
      return f"Movie {self.movie.title}"
  


class Theater(baseModel):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    city  = models.CharField(max_length=30,null=True,blank=True)
    total_screens = models.IntegerField()

    def __str__(self):
        return self.name
    
