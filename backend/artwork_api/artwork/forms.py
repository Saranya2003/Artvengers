from django import forms
from .models import ArtworkPost,Album

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = ArtworkPost
        fields = {'Title','artist_Name','Description','Tag','Artwork'}
        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'artist_Name': forms.Select(attrs={'class':'form-control'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
            'Tag': forms.TextInput(attrs={'class':'form-control'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = {'Album_Title','artist_Name','Description','Cover_Photo'}
        widgets = {
            'Album_Title': forms.TextInput(attrs={'class':'form-control'}),
            'artist_Name': forms.Select(attrs={'class':'form-control'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
        }