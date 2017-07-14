from rest_framework import serializers
from .GeoPointSerializer import GeoPointSerializer
from api.models.Itinerary import Itinerary


class ItinerarySerializer(serializers.ModelSerializer):
    geoPoints = GeoPointSerializer(many=True, read_only=True)

    class Meta:
        model = Itinerary
        fields = ('name', 'geoPoints')
