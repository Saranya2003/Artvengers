from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date

# Create your models here.
class ArtworkPost(models.Model):
    Title = models.CharField(max_length=255)
    artist_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    Description = models.TextField()
    Tag = models.CharField(max_length=255)
    Artwork = models.ImageField(null=True,blank=True,upload_to="media/img/")

    def get_absolute_url(self):
        return reverse('dashboard')
    

class Album(models.Model):
    Album_Title = models.CharField(max_length=255)
    artist_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    Description = models.TextField()
    Cover_Photo = models.ImageField(null=True,blank=True,upload_to="media/img/album_cover")

    def get_absolute_url(self):
        return reverse('dashboard')

class Comment(models.Model):
    post = models.ForeignKey(ArtworkPost,related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    comment = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return '%s - %s'%(self.post.title,self.name)
    
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_picture = models.ImageField(null=True,blank=True,upload_to="media/img/profile_pic")
    Instagram = models.CharField(max_length=255)
    Twitter = models.CharField(max_length=255)
    Facebook = models.CharField(max_length=255)
    def __str__(self):
        return str(self.user)