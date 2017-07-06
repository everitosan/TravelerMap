from django.db import models
from .Itinerary import Itinerary


class GeoPoint(models.Model):
    place = models.CharField(max_length=50, blank=False)
    activity = models.CharField(max_length=100, blank=False)
    dateTime = models.DateTimeField(auto_now=False, blank=False)
    coords = models.CharField(max_length=80, blank=False)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE)
    deleted = models.BooleanField(default=False)
