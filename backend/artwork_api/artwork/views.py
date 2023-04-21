from django.shortcuts import render
from rest_framework import generics
from django.views.generic import ListView,DetailView,CreateView, UpdateView

from .models import ArtworkPost,Album
from .serializers import ArtworkSerializer
from .forms import ArtworkForm


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

class AddArtwork(CreateView):
    model = ArtworkPost
    form_class = ArtworkForm
    template_name = 'artwork_upload.html'

class AddAlbum(CreateView):
    model = Album
    template_name = 'add_album.html'
    fields = '__all__'

class UpdateAlbum(UpdateView):
    model = Album
    template_name = 'update_album.html'
    fields = ['Title','Description','Tag']

class UpdateArtworks(UpdateView):
    model = Album
    template_name = 'update_artwork.html'
    fields = ['Title','Description']