from django.contrib import admin
from .models import ArtworkPost,Album,Comment
# Register your models here.
admin.site.register(ArtworkPost)
admin.site.register(Album)
admin.site.register(Comment)