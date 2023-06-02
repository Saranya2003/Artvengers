from rest_framework import serializers
from .models import ArtworkPost,Album
from django.contrib.auth.models import User

class ArtworkSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"

        model = ArtworkPost

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"