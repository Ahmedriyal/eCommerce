from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ClubJerseyDetails(models.Model):
    title = models.CharField(max_length=150)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image1 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image2 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image3 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image4 = models.ImageField(upload_to='img/', null=True, blank=True)
    authenticity = models.CharField(max_length=50, null=True, blank=True)
    team_badge = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    availability = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class NTJerseyDetails(models.Model):
    title = models.CharField(max_length=150)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image1 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image2 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image3 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image4 = models.ImageField(upload_to='img/', null=True, blank=True)
    authenticity = models.CharField(max_length=50, null=True, blank=True)
    team_badge = models.CharField(max_length=50, null=True, blank=True)
    description = models.CharField(max_length=500, null=True, blank=True)
    availability = models.BooleanField(default=True)



    def __str__(self):
        return self.title
