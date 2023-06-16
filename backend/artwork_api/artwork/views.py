from django.shortcuts import render, get_object_or_404
from rest_framework import generics,viewsets, permissions
from django.views.generic import ListView,DetailView,CreateView, UpdateView, TemplateView

from .models import ArtworkPost,Album, Comment, Tag
from .serializers import AlbumSerializer, ArtworkSerializer
from .forms import AlbumForm, ArtworkForm


# Create your views here.
class ListArtwork(generics.ListCreateAPIView):
    queryset = ArtworkPost.objects.all()
    serializer_class = ArtworkSerializer
    ordering =['-id']

class ListAlbum(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    ordering =['-id']
    
class DetailAlbum(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class DetailArtwork(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArtworkPost.objects.all()
    serializer_class = ArtworkSerializer

def home(request):
    return render(request,'home.html',{})

class ArtworkPostDetail(DetailView):
    model = ArtworkPost
    template_name = 'art_post_detail.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment'] = Comment.objects.all()
        return context

class ExploreView(ListView):
    model = ArtworkPost
    template_name = 'explore.html'
    ordering =['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        context['artwork'] = ArtworkPost.objects.all()
        return context
    
def explore(request):
    album_display = Album.objects.all()
    artwork_display = ArtworkPost.objects.all()
    ordering =['-id']
    
    return render(request,'explore.html',{"Album":album_display,"ArtworkPost":artwork_display,"ordering":ordering})

class DashboardView(ListView):
    model = ArtworkPost
    template_name = 'dashboard.html'
    ordering =['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        context['artwork'] = ArtworkPost.objects.all()
        return context

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

def SearchView(request):
    
    return render(request,'search_page.html',{})

def list_artwork_by_tag(request,tag_id):
    tag = get_object_or_404(Tag, id=tag_id)

    artwork = ArtworkPost.objects.filter(tags=tag)

    context = {
        "tag_name":tag.tag,
        "artwork":artwork
    }

    return render(request,"artwork_tag.html",context)

