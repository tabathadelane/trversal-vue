from django.db import models
from django.urls import reverse

# Create your models here.

class Trip(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name