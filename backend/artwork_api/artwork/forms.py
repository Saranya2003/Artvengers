from django import forms
from .models import ArtworkPost,Album,Comment

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = ArtworkPost
        fields = {'Title','artist_Name','Description','Tag','Artwork'}
        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'artist_Name': forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
            'Tag': forms.TextInput(attrs={'class':'form-control'}),
        }

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = {'Album_Title','artist_Name','Description','Cover_Photo'}
        widgets = {
            'Album_Title': forms.TextInput(attrs={'class':'form-control'}),
            'artist_Name': forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','comment')
        widgets = {
            'name' : forms.TextInput(attrs={'value':'','id':'user','type':'hidden'}),
            'comment' : forms.Textarea(),
        }
