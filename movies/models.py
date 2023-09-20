from django.db import models

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    genres = models.ManyToManyField(Genre)

    def __str__(self):
        return self.title