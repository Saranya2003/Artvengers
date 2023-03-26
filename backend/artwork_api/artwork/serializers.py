from rest_framework import serializers
from .models import ArtworkPost

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"

        model = ArtworkPost