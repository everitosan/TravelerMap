from rest_framework import viewsets
from api.models.Note import Note
from api.serializers.NoteSerializer import NoteSerializer


class NoteView(viewsets.ModelViewSet):
    queryset = Note.objects.filter(deleted=False)
    serializer_class = NoteSerializer
