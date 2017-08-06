from rest_framework import viewsets, status
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from api.models.Itinerary import Itinerary
from api.models.GeoPoint import GeoPoint
from api.serializers.ItinerarySerializer import ItinerarySerializer
from api.serializers.GeoPointSerializer import GeoPointSerializer
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


class ItineraryView(viewsets.ModelViewSet):
    queryset = Itinerary.objects.filter(deleted=False)
    serializer_class = ItinerarySerializer

    @detail_route(methods=['get'])
    def geopoints(self, request, pk=None):
        itinerary = get_object_or_404(Itinerary, pk=pk)
        geopoints_serializer = GeoPointSerializer(
            itinerary.geoPoints.filter(deleted=False).order_by('dateTime'),
            many=True)
        return Response(
            geopoints_serializer.data,
            content_type="application/json")

    @detail_route(methods=['post'])
    def remove(self, request, pk=None):
        try:
            itinerary = Itinerary.objects.get(pk=pk)
            itinerary.deleted = True
            itinerary.save()
            return Response(
                {"Status": "Deleted"},
                status=status.HTTP_200_OK,
                content_type="application/json"
            )
        except ObjectDoesNotExist:
            self.doesNotExist()

    @detail_route(methods=['post'])
    def addGeoPoint(self, request, pk=None):
        try:
            itinerary = Itinerary.objects.get(pk=pk)
            geopoint_seralizer = GeoPointSerializer(data=request.data)
            if geopoint_seralizer.is_valid():
                geopoint_seralizer.validated_data['itinerary'] = itinerary
                geopoint_seralizer.save()
                return Response(
                    geopoint_seralizer.data,
                    status=status.HTTP_200_OK,
                    content_type="application/json"
                )
            else:
                return Response(
                    geopoint_seralizer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                    content_type="application/json"
                )
        except ObjectDoesNotExist:
            self.doesNotExist()

    def doesNotExist(self):
        return Response(
            {"Status": "Itinerary not found"},
            status=status.HTTP_404_NOT_FOUND,
            content_type="application/json"
        )
