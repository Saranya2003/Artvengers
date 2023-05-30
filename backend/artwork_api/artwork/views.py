from django.shortcuts import render, get_object_or_404
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

    def get_context_data(self, *args, **kwargs):
        context = super(Artwork_Post_Detail, self).get_context_data()
        stuff = get_object_or_404(ArtworkPost,id=self.kwargs['pk'])
        context['artwork'] = ArtworkPost.objects.all()
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

class DashboardView(ListView):
    model = ArtworkPost
    template_name = 'dashboard.html'

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

class SearchArtwork(ListView):
    model = ArtworkPost
    template_name = 'search_page.html'