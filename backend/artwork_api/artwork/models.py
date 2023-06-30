from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from taggit.managers import TaggableManager

# Create your models here.
    
class ArtworkPost(models.Model):
    Title = models.CharField(max_length=255)
    artist_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    Description = models.TextField()
    Sensitive_content = models.BooleanField(default=False)
    Tags = TaggableManager()
    Artwork = models.FileField(blank=True,upload_to="media/img/")
    likes = models.ManyToManyField(User, related_name='artwork_post')
    #album = models.TextField()

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('dashboard')

    
class Album(models.Model):
    Album_Title = models.CharField(max_length=255)
    artist_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    Private_Album = models.BooleanField(default=False)
    memberpic = models.ManyToManyField(ArtworkPost, related_name='artwork_post')

    def get_absolute_url(self):
        return reverse('dashboard')

class Comment(models.Model):
    post = models.ForeignKey(ArtworkPost,related_name="comment", on_delete=models.CASCADE)
    artist_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    artwork_comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    email = models.EmailField()
    def __str__(self):
        return str(self.user)
    
