from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class ClubJerseyDetails(models.Model):
    title = models.CharField(max_length=150)

    Fan_Version = 'Fan Version'
    Player_Version = 'Player Version'

    type_choices = [
        (Fan_Version, 'Fan Version'),
        (Player_Version, 'Player Version'),
    ]
    type = models.CharField(max_length=50, choices=type_choices, null=True, blank=True)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image1 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image2 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image3 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image4 = models.ImageField(upload_to='img/', null=True, blank=True)
    authenticity = models.CharField(max_length=50, null=True, blank=True)
    team_badge = models.CharField(max_length=50, null=True, blank=True)
    availability = models.BooleanField(default=True)
    added_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def small_image1URL(self):
        try:
            url = self.small_image1.url
        except:
            url = ''
        return url

    @property
    def small_image2URL(self):
        try:
            url = self.small_image2.url
        except:
            url = ''
        return url

    @property
    def small_image3URL(self):
        try:
            url = self.small_image3.url
        except:
            url = ''
        return url

    @property
    def small_image4URL(self):
        try:
            url = self.small_image4.url
        except:
            url = ''
        return url



class NTJerseyDetails(models.Model):
    title = models.CharField(max_length=150)

    Fan_Version = 'Fan Version'
    Player_Version = 'Player Version'

    type_choices = [
        (Fan_Version, 'Fan Version'),
        (Player_Version, 'Player Version'),
    ]
    type = models.CharField(max_length=50, choices=type_choices, null=True, blank=True)
    price = models.CharField(max_length=50)
    image = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image1 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image2 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image3 = models.ImageField(upload_to='img/', null=True, blank=True)
    small_image4 = models.ImageField(upload_to='img/', null=True, blank=True)
    authenticity = models.CharField(max_length=50, null=True, blank=True)
    team_badge = models.CharField(max_length=50, null=True, blank=True)
    availability = models.BooleanField(default=True)
    added_time = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return self.title

    @property
    def small_image1URL(self):
        try:
            url = self.small_image1.url
        except:
            url = ''
        return url

    @property
    def small_image2URL(self):
        try:
            url = self.small_image2.url
        except:
            url = ''
        return url

    @property
    def small_image3URL(self):
        try:
            url = self.small_image3.url
        except:
            url = ''
        return url

    @property
    def small_image4URL(self):
        try:
            url = self.small_image4.url
        except:
            url = ''
        return url

