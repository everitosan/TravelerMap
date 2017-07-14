from django.contrib import admin
from .models import GeoPoint, Itinerary, Note

admin.site.register(GeoPoint)
admin.site.register(Itinerary)
admin.site.register(Note)
