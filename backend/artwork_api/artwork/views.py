from django.shortcuts import render, get_object_or_404
from rest_framework import generics,viewsets, permissions
from django.views.generic import ListView,DetailView,CreateView, UpdateView, TemplateView,DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin

from .models import ArtworkPost,Album, Comment
from .serializers import AlbumSerializer, ArtworkSerializer
from .forms import AlbumForm, ArtworkForm, CommentForm
from taggit.models import Tag

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

    form_class = CommentForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #(context['artwork'] = ArtworkPost.objects.all()
       # print(context)
        #print(context['artworkpost'].Tags.names())
        context['comment'] = Comment.objects.all()
        
        return context
class AlbumView(ListView):
    model = Album
    template_name = 'album_view.html'

class ExploreView(ListView):
    model = ArtworkPost
    template_name = 'explore.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['album'] = Album.objects.all()
        context['artwork'] = ArtworkPost.objects.all().order_by('-pk')
        context['Tags'] = Tag.objects.all()
        #print(context['Tags'][0])
        #print(context['artwork'])
        #print(context['artwork'][0].Tags.names())
        #print(context['artwork'].order_by('-pk'))
        return context

class DashboardView(ListView):
    model = ArtworkPost
    template_name = 'dashboard.html'
    ordering =['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        context['artwork'] = ArtworkPost.objects.all().order_by('-pk')
        return context

class AddArtwork(CreateView):
    model = ArtworkPost
    form_class = ArtworkForm
    template_name = 'artwork_upload.html'

class AddAlbum(CreateView):
    model = Album
    form_class = AlbumForm
    template_name = 'add_album.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        context['artwork'] = ArtworkPost.objects.all().order_by('-pk')
        return context

class UpdateAlbum(UpdateView):
    model = Album
    template_name = 'update_album.html'
    fields = ['Title','Cover_Photo']

class UpdateArtworks(UpdateView):
    model = ArtworkPost
    template_name = 'update_artwork.html'
    fields = ['Title','Description','Tags','Artwork']

def SearchView(request):
    
    return render(request,'search_page.html',{})

class TagsView(ListView):
    model = ArtworkPost
    template_name = 'Tags_view.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.kwargs['Tag'])
        context['album'] = Album.objects.all()

        context['artwork'] = ArtworkPost.objects.filter(Tags__name__in=[self.kwargs['Tag']]).order_by('-pk')
        
       # print(context['artwork'][0].Tags.names())
        context['Tags'] = Tag.objects.all()
        #print(context['Tags'][0])
        #print(context['artwork'])
       # print(context['artwork'].order_by('-pk'))
        return context

class DeleteArtwork(SuccessMessageMixin,DeleteView):
    model = ArtworkPost
    success_url = reverse_lazy('dashboard')
    success_message = "Your artwork has been deleted successfully."
    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(DeleteArtwork, self).delete(request, *args, **kwargs)