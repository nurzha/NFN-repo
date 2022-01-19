from django.db import models
from django.db.models.fields import EmailField

from Django.portfolio_project.listing.models import TYPE_CHOICES, Listing

# Create your models here.

class Booking(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    checkin = models.DateTimeField(auto_now=False, auto_now_add=False)
    checkout = models.DateTimeField(auto_now=False, auto_now_add=False)
    numguest = models.IntegerField()
    status = models.CharField(max_length=10, choices=TYPE_CHOICES)
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE)

class Guest(models.Model):
    firsname = models.CharField(max_length= 100, blank=False, null=False)
    lastname = models.CharField(max_length= 100, blank=False, null=False)
    email =models.EmailField(max_length= 100, blank=False, null=False)

