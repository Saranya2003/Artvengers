from django import forms
from .models import ArtworkPost,Album,Comment

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = ArtworkPost
        fields = {'Title','artist_Name','Description','Sensitive_content','Artwork'}
        fields_order = ['Title','artist_Name','Description','Sensitive_content','Artwork']
        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'artist_Name': forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
        }
        

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = {'Album_Title','artist_Name','Private_Album'}
        fields_order = ['Album_Title','artist_Name','Private_Album']
        widgets = {
            'Album_Title': forms.TextInput(attrs={'class':'form-control'}),
            'artist_Name': forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
        }
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('artist_Name','comment')
        widgets = {
            'artist_Name' : forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            'comment' : forms.Textarea(attrs={'class':'form-control'}),
        }
