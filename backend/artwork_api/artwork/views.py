from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken

from .models import ArtworkPost
from .serializers import ArtworkSerializer


# Create your views here.
class ListArtwork(generics.ListCreateAPIView):
    queryset = ArtworkPost.objects.all()
    serializer_class = ArtworkSerializer
    ordering =['-id']

class DetailArtwork(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtworkPost.objects.all()
    serializer_class = ArtworkSerializer
