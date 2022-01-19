from django.db import models
from djmoney.models.fields import MoneyField

from Django.portfolio_project.booking.models import Guest

# Create your models here.
class Payments(models.Model):
    card_holder = models.CharField(max_length= 100, blank=False, null=False)
    card_num = models.IntegerField(blank=False, null=False)
    card_exp_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=False, null=False)
    paypal = models.BooleanField()
    amount = MoneyField(max_digits=10, decimal_places=2, 
            default_currency='USD')
    guest_id = models.ForeignKey(Guest, on_delete=models.CASCADE)