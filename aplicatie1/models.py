from django.db import models

# Create your models here.

class Location(models.Model):

    country = models.Charfield(max.length=100)
    city =