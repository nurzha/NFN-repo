from django.db import models
from Django.portfolio_project.booking.models import Booking, Guest

from Django.portfolio_project.host.models import Host

# Create your models here.
class Review(models.Model):
    score = models.IntegerField(blank=False, null=False)
    comment = models.CharField(max_length= 280, blank=False, null=False)
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)
    host_id = models.ForeignKey(Host, on_delete=models.CASCADE)
    booking_id = models.ForeignKey(Booking, on_delete=models.CASCADE)