from django.db import models
from .GeoPoint import GeoPoint


class Note(models.Model):
    color = models.CharField(max_length=9, default="#885736")
    content = models.CharField(max_length=100, blank=False, null=False)
    geoPoint = models.ForeignKey(GeoPoint, on_delete=models.CASCADE, related_name="notes")
    deleted = models.BooleanField(default=False)
