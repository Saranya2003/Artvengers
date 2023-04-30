from django.shortcuts import render
from rest_framework import generics,viewsets, permissions
from django.views.generic import ListView,DetailView,CreateView, UpdateView

from .models import ArtworkPost,Album
from .serializers import ArtworkSerializer
from .forms import AlbumForm, ArtworkForm


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

class ExploreView(ListView):
    model = ArtworkPost
    template_name = 'explore.html'

class DashboardView(ListView):
    model = ArtworkPost
    template_name = 'dashboard.html'

class AddArtwork(CreateView):
    model = ArtworkPost
    form_class = ArtworkForm
    template_name = 'artwork_upload.html'

class AddAlbum(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'

class UpdateAlbum(UpdateView):
    model = Album
    template_name = 'update_album.html'
    fields = ['Title','Description','Cover_Photo']

class UpdateArtworks(UpdateView):
    model = ArtworkPost
    template_name = 'update_artwork.html'
    fields = ['Title','Description','Tag','Artwork']