from django.db import models
from django.utils.text import slugify
import requests
from io import BytesIO
from django.core import files

# Create your models here.
class Genre(models.Model):
    title = models.CharField(max_length=30)
    slug = models.SlugField(null=False, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.title.replace(" ", "")
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

class Rating(models.Model):
    source = models.CharField(max_length=50)
    rated = models.CharField(max_length=10)

    def __str__(self):
        return self.source

    
class MovieSeries(models.Model):
    Title = models.CharField(max_length=100)
    Year = models.CharField(max_length=5, blank=True)
    Ratings = models.ManyToManyField(Rating)
    Genre = models.ManyToManyField(Genre, blank=True)
    Plot = models.CharField(max_length=1000)
    Lang = models.CharField(max_length=100, blank=True)
    Poster = models.ImageField(upload_to='cameo')
    Poster_url = models.URLField(blank=True)
    Type = models.CharField(max_length=100, blank=True)
    Seasons = models.CharField(max_length=3, blank=True)
    imdbRating = models.CharField(max_length=5, blank=True)
    imdbID = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.Title

    # saving the poster image to db
    def save(self, *args, **kwargs):
        if self.Poster == '' and self.Poster_url !='':
            resp = requests.get(self.Poster_url)
            pb = BytesIO()
            pb.write(resp.content)
            pb.flush()
            file_name = self.Poster_url.split("/")[-1]
            self.Poster.save(file_name, files.File(pb), save=False)

        return super().save(*args, **kwargs)


