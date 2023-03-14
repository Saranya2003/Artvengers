from django.shortcuts import render
from rest_framework import generics
from .models import ArtworkPost
from .serializers import ArtworkSerializer

# Create your views here.
class ListArtwork(generics.ListCreateAPIView):
    queryset = ArtworkPost.objects.all()
    serializer_class = ArtworkSerializer

class DetailArtwork(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtworkPost.objects.all()
    serializer_class = ArtworkSerializer