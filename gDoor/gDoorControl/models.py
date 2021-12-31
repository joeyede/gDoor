from django.db import models

class HomeLocations(models.Model):
    home_lat = models.FloatField(null=True, blank=True, default=None)
    home_long =  models.FloatField(null=True, blank=True, default=None)

