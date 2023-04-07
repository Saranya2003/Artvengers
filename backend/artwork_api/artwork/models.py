from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime,date

# Create your models here.
class ArtworkPost(models.Model):
    artTitle = models.CharField(max_length=255)
    artistName = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    imageUploader = models.ImageField(null=True,blank=True,upload_to="media/img/")
    description = models.TextField()