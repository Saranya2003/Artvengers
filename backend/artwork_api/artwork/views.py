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
from django.db.models import Count, Q
# Create your views here.

def addtoalbum(request,pk):
    if request.method == 'POST':
        if request.POST['Album_Title'] is not None:
            albumid = request.POST['Album_Title']
        elif request.POST['Album_Titlemob'] is not None:
            albumid = request.POST['Album_Titlemob']
       # print("albumid is", albumid)
        albumcontent = Album.objects.get(pk=albumid)
        
        form = UpdateAlbumForm(request.POST, instance=albumcontent)
        oldalbumname = albumcontent.Album_Title
        print(request.POST)
        if form.is_valid():
            
            form.instance.artist_Name = request.user
            form.instance.Album_Title = oldalbumname
           # form.instance.Album_Title = albumid
            memlistid = request.POST['colartworkpost_id']
           

            print(memlistid)
            print("Before:",form.instance.memberpic.all())
            form.instance.memberpic.add(ArtworkPost.objects.get(pk=int(memlistid)))
            form.instance.save() 
            print("After:", form.instance.memberpic.all())
            print("Albumcontent:", albumcontent.memberpic.all())
           # NewAlbum.memberpic.all()
           # print(NewAlbum.memberpic.all())
            
            
            #form.save_m2m()
            return HttpResponseRedirect(reverse('artwork_detail',args=[str(pk)]))
        else:
            print(form.errors.as_data())
            print("can't upload")

def insertalbum(request):
    print(request.POST)
   
    if request.method == 'POST':
       # print(request.FILES)
        form = AlbumForm(request.POST)
        if form.is_valid():
            form.instance.artist_Name = request.user
            memlistid = request.POST['memberpiclist'].split(",")


            
            
            form.save()
            for i in memlistid:
                #print(i)          
                form.instance.memberpic.add(ArtworkPost.objects.get(pk=int(i)))

           # NewAlbum.memberpic.all()
           # print(NewAlbum.memberpic.all())
            
            
            #form.save_m2m()
            return HttpResponseRedirect(reverse('explore'))
        else:
            print(form.errors.as_data())
            print("can't upload")


def insertartwork(request):
    if request.method == 'POST':
        form = ArtworkForm(request.POST)
        if form.is_valid():
            artwork = form.save(commit=False)
            artwork.Artwork = request.FILES['Artwork']
            
            if form.fields.get('artist_Name').required:
                artwork.artist_Name = request.user
            
            artwork.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('explore'))
        else:
            print(form.errors.as_data())
            print("Can't upload")

def updateartworkpost(request, pkreq):
    print(request.POST)
    artcontent = ArtworkPost.objects.get(pk=pkreq)
    if request.method == 'POST':
        
        
        form = ArtworkForm(request.POST, instance=artcontent)
        if form.is_valid():
            UpdateArtwork = form.save(commit=False)
            UpdateArtwork.artist_Name = request.user
            
            #print(NewArtwork)
           
           # print(UpdateArtwork)
            UpdateArtwork.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('explore'))
        else:
            print(form.errors.as_data())
            print("can't edit")       

def updatealbum(request, pkreq):
    print(request.POST)
    albumcontent = Album.objects.get(pk=pkreq)
    if request.method == 'POST':
        
        
        form = AlbumForm(request.POST, instance=albumcontent)
        if form.is_valid():

            form.instance.artist_Name = request.user
            memlistid = request.POST['memberpiclist'].split(",")
           
            #print(NewAlbum)
            form.instance.memberpic.clear()
            
            for i in memlistid:
                #print(i)          
                form.instance.memberpic.add(ArtworkPost.objects.get(pk=int(i)))
            print("memberpic", form.instance.memberpic.all())
        
            form.instance.save()
            #form.instance.save_m2m()
            return HttpResponseRedirect(reverse('explore'))
        else:
            print(form.errors.as_data())
            print("can't edit")       

def LikeView(request,pk):
    #print("Like Request post is", request.POST)
    artwork_post = get_object_or_404(ArtworkPost, pk = request.POST.get('artworkpost_id'))
    if artwork_post.likes.filter(id=request.user.id).exists():
        artwork_post.likes.remove(request.user)
    else:
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
   # print(request.POST)
    post = get_object_or_404(ArtworkPost, pk = request.POST.get('addcommentbutton'))
    
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = form.save(commit=False)
        comment.artist_Name = request.user
        if form.is_valid():
           
           comment.post = post
           comment.save()
           return HttpResponseRedirect(reverse('artwork_detail',args=[str(pk)]))
        else:
           print(form.errors.as_data())
           print("can't post comment")  

            

class ArtworkPostDetail(DetailView):
    model = ArtworkPost
    form_class = CommentForm
    template_name = 'art_post_detail.html' 
    
    
        
    def get_context_data(self, **kwargs):
       
        context = super().get_context_data(**kwargs)
        stuff = get_object_or_404(ArtworkPost, id=self.kwargs['pk'])
        liked = False
        total_likes = stuff.total_likes()
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        context['likes'] = total_likes
        context['liked_post'] = liked
        context['album'] = Album.objects.all()
     


        context['comments'] = Comment.objects.filter(post_id=self.kwargs['pk'])
        context['form'] = CommentForm()
        
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
        
        context['album'] = Album.objects.all().order_by('-pk')
        context['artwork'] = ArtworkPost.objects.all().order_by('-pk')
        context['tags'] = Tag.objects.annotate(artwork_count=Count('artworkpost')).filter(artwork_count__gt=0).order_by('-artwork_count')
        
        return context

    
class Taglist(ListView):
    model = ArtworkPost
    template_name = 'Tags_mobile.html'
    ordering = ['-id']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Tags'] = Tag.objects.annotate(artwork_count=Count('artworkpost')).filter(artwork_count__gt=0).order_by('-artwork_count')
        return context
class DashboardView(ListView):
    model = ArtworkPost
    template_name = 'dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['album'] = Album.objects.all().order_by('-pk')
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

    def get_context_data(self, **kwargs):
        piclist=[]
        context = super().get_context_data(**kwargs)
        album = self.get_object()  # Get the current album being updated
        context['album'] = album
        context['artwork'] = album.memberpic.all().order_by('-pk')
 
        
        # Get the other user's artwork
        other_user_artwork = ArtworkPost.objects.exclude(artist_Name=album.artist_Name)
        context['other_user_artwork'] = other_user_artwork
        if context['artwork'] is not None:
            for i in context['artwork']:
                print(i.pk)
                piclist.append(i.pk)
            context['piclist'] = piclist
            #context['artwork'] = ArtworkPost.objects.all().order_by('-pk')
        return context

class UpdateArtworks(UpdateView):
    model = ArtworkPost
    form_class = UpdateArtworkForm
    template_name = 'update_artwork.html'

class SearchView(ListView):
    model = ArtworkPost
    template_name = 'search_page.html'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['album'] = Album.objects.filter(Q(Album_Title__icontains=self.request.GET['keyword'])).order_by('pk').distinct()
        context['artwork'] = ArtworkPost.objects.filter(Q(Title__icontains=self.request.GET['keyword'])| Q(Tags__name__icontains=self.request.GET['keyword'])).order_by('pk').distinct()
        context['Tags'] = Tag.objects.all()
       
        return context
    
class SearchMobileView(ListView):
    model = ArtworkPost
    template_name = 'search_mobile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.annotate(artwork_count=Count('artworkpost')).filter(artwork_count__gt=0).order_by('-artwork_count')
       
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
    