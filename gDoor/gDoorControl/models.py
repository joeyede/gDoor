from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model


def get_sentinel_user():
    return get_user_model().objects.get_or_create(username='deleted')[0]

class DoorToggleRecord(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        models.SET(get_sentinel_user),
    )
    toggle_date = models.DateTimeField('date published')
    pre_toggle_door_state = models.CharField(max_length = 40)

#settings.AUTH_USER_MODEL


class HomeLocations(models.Model):
    home_lat = models.FloatField(null=True, blank=True, default=None)
    home_long =  models.FloatField(null=True, blank=True, default=None)

