from django.shortcuts import redirect, render, get_object_or_404,HttpResponse
from rest_framework import generics,viewsets, permissions
from django.views.generic import ListView,DetailView,CreateView, UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from django.db.models import Q
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormMixin
from django.http import HttpResponseRedirect

from .models import ArtworkPost,Album, Comment
from .serializers import AlbumSerializer, ArtworkSerializer
from .forms import AlbumForm, ArtworkForm, CommentForm,UpdateArtworkForm,UpdateAlbumForm
from taggit.models import Tag

# Create your views here.
def sensitive_toggle(request):
    sensitive = ArtworkPost.objects.get(id=request.POST['id'])
    sensitive.Sensitive_content = request.POST['sensitive']=='true'
    sensitive.save()
    return HttpResponse('success')

def private_toggle(request):
    private = Album.objects.get(id=request.POST['id'])
    private.Private_Album = request.POST['private']=='true'
    private.save()
    return HttpResponse('success')

def LikeView(request,pk):
    #print("Like Request post is", request.POST)
    artwork_post = get_object_or_404(ArtworkPost, pk = request.POST.get('artworkpost_id'))
    artwork_post.likes.add(request.user)
    return HttpResponseRedirect(reverse('artwork_detail',args=[str(pk)]))



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

def uploadPage(request):
    return render(request,'upload.html',{})

def post_comment(request, pk):
    print(request.POST)
    post = get_object_or_404(ArtworkPost, pk = request.POST.get('addcommentbutton'))
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
           comment = form.save(commit=False)
           comment.post = post
           comment.save()

           return HttpResponseRedirect(reverse('artwork_detail',args=[str(pk)]))

class ArtworkPostDetail(DetailView):
    model = ArtworkPost
    form_class = CommentForm
    template_name = 'art_post_detail.html' 
    
    
        
    def get_context_data(self, **kwargs):
       
        context = super().get_context_data(**kwargs)
        #print(context['form'])
        #(context['artwork'] = ArtworkPost.objects.all()
       # print(context)
        #print(context['artworkpost'].Tags.names())
        stuff = get_object_or_404(ArtworkPost, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context['likes'] = total_likes
        context['comments'] = Comment.objects.filter(post_id=self.kwargs['pk'])
        context['form'] = CommentForm()
        #print("POST is", self.request.GET)
       # print("POSTED")
        #print(context['comments'])
        return context
class AlbumView(ListView):
    model = Album
    template_name = 'album_view.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #print(self.kwargs['pk'])
        context['album'] = Album.objects.filter(pk=self.kwargs['pk']).order_by('-pk')
        print(context['album'][0].Album_Title)
        #print(context['album'][0].memberpic.all())
        context['artwork'] = context['album'][0].memberpic.all().order_by('-pk')
        
        context['Tags'] = Tag.objects.all()
        return context

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
class Taglist(ListView):
    model = ArtworkPost
    template_name = 'Tags_mobile.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
    form_class = UpdateAlbumForm
    template_name = 'update_album.html'

class UpdateArtworks(UpdateView):
    model = ArtworkPost
    form_class = UpdateArtworkForm
    template_name = 'update_artwork.html'

class SearchView(ListView):
    model = ArtworkPost
    template_name = 'search_page.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.GET['keyword'])

        context['album'] = Album.objects.all()
        context['artwork'] = ArtworkPost.objects.filter(Q(Title__icontains=self.request.GET['keyword'])| Q(Tags__name__icontains=self.request.GET['keyword'])).order_by('pk').distinct()
        print(context['artwork'])
        context['Tags'] = Tag.objects.all()
       
        return context
class SearchMobileView(ListView):
    model = ArtworkPost
    template_name = 'search_mobile.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.GET['keyword'])

        context['album'] = Album.objects.all()
        context['artwork'] = ArtworkPost.objects.filter(Q(Title__icontains=self.request.GET['keyword'])| Q(Tags__name__icontains=self.request.GET['keyword'])).order_by('pk').distinct()
        print(context['artwork'])
        context['Tags'] = Tag.objects.all()
       
        return context

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
        context['SelectTag'] = self.kwargs['Tag']
        #print(context['Tags'][0])
        #print(context['artwork'])
       # print(context['artwork'].order_by('-pk'))
        return context

class DeleteArtwork(DeleteView):
    model = ArtworkPost
    template_name = 'delete_artwork.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        context['artwork'] = ArtworkPost.objects.all()
        context['comment'] = Comment.objects.all()
        return context
    
class DeleteAlbum(DeleteView):
    model = Album
    template_name = 'delete_album.html'
    success_url = reverse_lazy('dashboard')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = Album.objects.all()
        
        return context
    