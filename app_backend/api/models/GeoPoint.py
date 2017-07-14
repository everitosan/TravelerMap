from django.db import models
from .Itinerary import Itinerary


class GeoPoint(models.Model):
    place = models.CharField(max_length=50, null=False, blank=False)
    activity = models.CharField(max_length=100, null=False, blank=False)
    dateTime = models.DateTimeField(auto_now=False, null=False, blank=False)
    coords = models.CharField(max_length=80, null=False, blank=False)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, related_name="geoPoints")
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.activity
