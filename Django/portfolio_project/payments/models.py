from django.db import models

# Create your models here.
class Payment(models.Model):
    card_holder = models.CharField(max_length= 100, blank=False, null=False)
    card_num = models.IntegerField(max_length= 16, blank=False, null=False)
    card_exp_date = models.DateField(
        auto_now=False, auto_now_add=False, blank=False, null=False)