from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date
from taggit.managers import TaggableManager
from django_resized import ResizedImageField
from easy_thumbnails.fields import ThumbnailerImageField


# Create your models here.
    
class ArtworkPost(models.Model):
    Title = models.CharField(max_length=100)
    artist_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    Description = models.TextField()
    Sensitive_content = models.BooleanField(default=False)
    Tags = TaggableManager()
    Artwork = ThumbnailerImageField(blank=True,upload_to="media/img/")
    likes = models.ManyToManyField(User, related_name='artwork_post')
    #album = models.TextField()

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('dashboard')

    
class Album(models.Model):
    Album_Title = models.CharField(max_length=100)
    artist_Name = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    Private_Album = models.BooleanField(default=False)
    memberpic = models.ManyToManyField(ArtworkPost, related_name='artwork_post',blank=True)

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
    bio = models.TextField()
    profile_picture = ResizedImageField(size=[180, 180], crop=['middle', 'center'],upload_to="media/img/profile_pic")
    Instagram = models.CharField(max_length=255)
    Twitter = models.CharField(max_length=255)
    Facebook = models.CharField(max_length=255)
    def __str__(self):
        return str(self.user)
    