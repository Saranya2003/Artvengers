from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date

# Create your models here.
class ArtworkPost(models.Model):
    Title = models.CharField(max_length=255)
    artistName = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    Description = models.TextField()
    Tag = models.CharField(max_length=255)
    Artwork = models.ImageField(null=True,blank=True,upload_to="media/img/")
    

class Album(models.Model):
    Title = models.CharField(max_length=255)
    artistName = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    Description = models.TextField()
    CoverPhoto = models.ImageField(null=True,blank=True,upload_to="media/img/")
