from rest_framework import serializers
from .models import ArtworkPost

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'artTitle',
            'artistName',
            'imageUploader',
            'description',
        )

        model = ArtworkPost