from django.shortcuts import render
from rest_framework import generics
from django.views.generic import ListView,DetailView

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

def home(request):
    return render(request,'home.html',{})

class Artwork_Post_List(ListView):
    model = ArtworkPost
    template_name = 'art_post_list.html'

class Artwork_Post_Detail(DetailView):
    model = ArtworkPost
    template_name = 'art_post_detail.html' 

def explore(request):
    return render(request,'explore.html')

def dashboard(request):
    return render(request,'dashboard.html')

