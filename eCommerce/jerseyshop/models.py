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


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    email = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return str(self.id)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    club_jersey = models.ForeignKey(ClubJerseyDetails, on_delete=models.SET_NULL, null=True, blank=True)
    national_jersey = models.ForeignKey(NTJerseyDetails, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)

    S = 'S'
    M = 'M'
    L = 'L'
    XL = 'XL'
    XXL = 'XXL'

    size_choices = [
        (S, 'S'),
        (M, 'M'),
        (L, 'L'),
        (XL, 'XL'),
        (XXL, 'XXL'),
    ]
    size = models.CharField(max_length=10, choices=size_choices, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class ShippingInfo(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    mobileNo = models.IntegerField(default=0, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True, null=True, blank=True)

