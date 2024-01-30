from django.db import models

# Create your models here.
class Piss(models.Model):
    longitude = models.DecimalField(max_digits=30, decimal_places=15)
    latitude = models.DecimalField(max_digits=30, decimal_places=15)
    text = models.CharField(max_length=200)

    def __str__(self):
        return self.text
    