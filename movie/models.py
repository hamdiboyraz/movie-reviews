from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='movie/images/')
    url = models.URLField(blank=True) #Each movie may not have URLs so we specify True to indicate this field is optional.
