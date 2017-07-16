from .NoteSerializer import NoteSerializer
from rest_framework import serializers
from api.models.GeoPoint import GeoPoint


class GeoPointSerializer(serializers.ModelSerializer):
    # notes = NoteSerializer(many=True, read_only=True)

    class Meta:
        model = GeoPoint
        # fields = ('id', 'place', 'activity', 'dateTime', 'coords', 'notes', 'deleted')
        fields = ('id', 'place', 'activity', 'dateTime', 'coords')
