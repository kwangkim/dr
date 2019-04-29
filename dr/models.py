from django.db import models
# Create your models here.
# https://www.filmsite.org/genres.html
class Director(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Movie(models.Model):
    GENRE_CHOICES=(
        ('ACT','Action'),
        ('ADV','Adventure'),
        ('COM','Comedy'),
        ('CRI','Crime and Ganster'),
        ('DRA','Drama'),
        ('HOR,','Horror'),
        ('SCI','Sceience Fiction'),
    )
    title = models.CharField(max_length=100)
    genre = models.CharField(max_length=3, choices=GENRE_CHOICES)
    # For simplicy, we only allow one director.
    # Ref: https://docs.djangoproject.com/en/2.1/topics/db/examples/
    director = models.ForeignKey(Director,on_delete=models.SET_NULL,default=None, blank=True, null=True)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('title',)