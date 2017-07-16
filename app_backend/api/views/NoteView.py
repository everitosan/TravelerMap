from rest_framework import viewsets, status
from api.models.Note import Note
from api.serializers.NoteSerializer import NoteSerializer
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.filter(deleted=False)
    serializer_class = NoteSerializer

    @detail_route(methods=['post'])
    def remove(self, request, pk=None):
        note = get_object_or_404(Note, pk=pk)
        note.deleted = True
        note.save()

        return Response(
            NoteSerializer(note).data,
            status=status.HTTP_200_OK,
            content_type="application/json"
        )
