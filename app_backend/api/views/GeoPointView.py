from rest_framework import viewsets
from api.models.GeoPoint import GeoPoint
from api.serializers.GeoPointSerializer import GeoPointSerializer


class GeoPointView(viewsets.ModelViewSet):
    queryset = GeoPoint.objects.filter(deleted=False)
    serializer_class = GeoPointSerializer
