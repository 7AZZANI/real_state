from cgi import print_exception
from turtle import title
from django.db import models





class Listing(models.Model):
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    num_bedrooms = models.IntegerField()
    num_bathrooms = models.IntegerField()
    square_footage = models.IntegerField()
    adress = models.CharField(max_length=70)

    def __str__(self):
        return self.title
