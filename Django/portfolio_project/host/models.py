from django.db import models

# Create your models here.


class Host(models.Model):
    name = models.CharField(max_length=100, null=False)
    email = models.EmailField(max_length=100, null=False)
    superhost = models.CharField(max_length=100, null=False)
