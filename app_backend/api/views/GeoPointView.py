from rest_framework import viewsets, status
from api.models.GeoPoint import GeoPoint
from api.models.Note import Note
from api.serializers.GeoPointSerializer import GeoPointSerializer
from api.serializers.NoteSerializer import NoteSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404


class GeoPointView(viewsets.ModelViewSet):
    queryset = GeoPoint.objects.filter(deleted=False)
    serializer_class = GeoPointSerializer

    @detail_route(methods=['get'])
    def notes(self, request, pk=None):
        geopoint = get_object_or_404(GeoPoint, pk=pk)
        note_seralizer = NoteSerializer(geopoint.notes.filter(deleted=False), many=True)
        return Response(
            note_seralizer.data,
            content_type="application/json"
        )

    @detail_route(methods=['post'])
    def remove(self, request, pk=None):
        try:
            geoPoint = GeoPoint.objects.get(pk=pk)
            geoPoint.deleted = True
            geoPoint.save()
            return Response(
                {"Status": "Deleted"},
                status=status.HTTP_200_OK,
                content_type="application/json")
        except ObjectDoesNotExist:
            return self.doesNotExist()

    @detail_route(methods=['post'])
    def addNote(self, request, pk=None):
        try:
            geoPoint = GeoPoint.objects.get(pk=pk)
            note_serializer = NoteSerializer(data=request.data)
            if note_serializer.is_valid():
                note_serializer.validated_data['geoPoint'] = geoPoint
                note_serializer.save()
                return Response(
                    note_serializer.data,
                    status=status.HTTP_200_OK,
                    content_type="application/json")
            else:
                return Response(
                    note_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST,
                    content_type="application/json"
                )
        except ObjectDoesNotExist:
            return self.doesNotExist()

    def doesNotExist(self):
        return Response(
            {"Error": "GeoPoint not found"},
            status=status.HTTP_404_NOT_FOUND,
            content_type="application/json")
