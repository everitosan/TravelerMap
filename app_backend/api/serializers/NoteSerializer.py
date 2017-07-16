from rest_framework import serializers
from api.models.Note import Note


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'color', 'content', 'deleted')
