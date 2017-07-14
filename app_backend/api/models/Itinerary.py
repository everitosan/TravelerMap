from django.db import models


class Itinerary(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return self.name
