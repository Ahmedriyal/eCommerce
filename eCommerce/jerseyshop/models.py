from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ClubJerseyDetails(models.Model):
    title = models.CharField(max_length=150)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', null=True, blank=True)

    # In_Stock = 'In Stock'
    # Out_of_Stock = 'Out of Stock'
    # choices = [
    #     (In_Stock, 'In Stock'),
    #     (Out_of_Stock, 'Out of Stock'),
    # ]
    # availabilty = models.CharField(max_length=50, choices=choices)
    description = models.CharField(max_length=500)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class NTJerseyDetails(models.Model):
    title = models.CharField(max_length=150)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    availability = models.BooleanField(default=True)
    description = models.CharField(max_length=500)


    def __str__(self):
        return self.title

