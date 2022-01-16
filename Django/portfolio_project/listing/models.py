from django.db import models
from host.models import Host


TYPE_CHOICES = (
    ('Daily', 'Daily'),
    ('Monthly', 'Monthly')
)

# Create your models here.


class Listing(models.Model):
    address = models.TextField(max_length=100, null=False)
    num_bedrooms = models.IntegerField(max_length=2, null=False)
    max_guests = models.IntegerField(max_length=2, null=False)
    type_of = models.CharField(max_length=10, choices=TYPE_CHOICES)
    email = models.EmailField(max_length=100, null=False)
    host_name = models.ForeignKey(Host, on_delete=models.CASCADE)
