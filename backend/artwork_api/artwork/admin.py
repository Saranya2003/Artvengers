from django.contrib import admin
from .models import ArtworkPost,Album,Comment,Profile,Tag
# Register your models here.
admin.site.register(ArtworkPost)
admin.site.register(Album)
admin.site.register(Comment)
admin.site.register(Profile)
admin.site.register(Tag)