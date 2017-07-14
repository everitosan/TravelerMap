from rest_framework import viewsets
from api.models.Itinerary import Itinerary
from api.serializers.ItinerarySerializer import ItinerarySerializer


class ItineraryView(viewsets.ModelViewSet):
    queryset = Itinerary.objects.filter(deleted=False)
    serializer_class = ItinerarySerializer
