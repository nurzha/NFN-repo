from django.db import models
from django.db.models.fields import EmailField

# Create your models here.

class Booking(models.Model):
    date = models.DateTimeField(auto_now=False, auto_now_add=False)
    checkin = models.DateTimeField(auto_now=False, auto_now_add=False)
    checkout = models.DateTimeField(auto_now=False, auto_now_add=False)
    numguest = models.IntegerField()
    
class Guest(models.Model):
    firsname = models.CharField(max_length= 100, blank=False, null=False)
    lastname = models.CharField(max_length= 100, blank=False, null=False)
    email =models.EmailField(max_length= 100, blank=False, null=False)
    booking_fk = models.ForeignKey(
        Booking,
        on_delete=models.CASCADE
    )
