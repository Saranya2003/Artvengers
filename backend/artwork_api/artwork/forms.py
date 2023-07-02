from django import forms
from .models import ArtworkPost,Album,Comment
from taggit.forms import *
from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget

class ArtworkForm(forms.ModelForm):
    Tags = TagField()
    class Meta:
        model = ArtworkPost
        fields = {'Title','artist_Name','Description','Sensitive_content','Tags','Artwork'}
        field_order = ['Title','artist_Name','Description','Sensitive_content','Tags','Artwork']
        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'artist_Name': forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
            'Sensitive_content': forms.CheckboxInput(
                    attrs={"class": "form-check-input", "id": "flexSwitchCheckChecked"}),
        }
        

class AlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = {'Album_Title','artist_Name','Private_Album', 'memberpic'}
        field_order = ['Album_Title','artist_Name','Private_Album','memberpic']
        widgets = {
            'Album_Title': forms.TextInput(attrs={'class':'form-control'}),
            'artist_Name': forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            'Private_Album': forms.CheckboxInput(
                    attrs={"class": "form-check-input", "id": "flexSwitchCheckChecked"}),
        }

class UpdateArtworkForm(forms.ModelForm):
    Tags = TagField()
    class Meta:
        model = ArtworkPost
        fields = {'Title','artist_Name','Description','Sensitive_content','Tags','Artwork'}
        field_order = ['Title','artist_Name','Description','Sensitive_content','Tags','Artwork']
        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'artist_Name': forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
            'Sensitive_content': forms.CheckboxInput(
                    attrs={"class": "form-check-input", "id": "flexSwitchCheckChecked"}),
           
        }
        

class UpdateAlbumForm(forms.ModelForm):
    
    class Meta:
        model = Album
        fields = {'Album_Title','artist_Name','Private_Album', 'memberpic'}
        field_order = ['Album_Title','artist_Name','Private_Album','memberpic']
        widgets = {
            'Album_Title': forms.TextInput(attrs={'class':'form-control'}),
            'artist_Name': forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            'Private_Album': forms.CheckboxInput(
                    attrs={"class": "form-check-input", "id": "flexSwitchCheckChecked"}),
        }       

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('artist_Name','artwork_comment')
        widgets = {
            'artist_Name' : forms.TextInput(attrs={'class':'form-control','value':'','id':'user','type':'hidden'}),
            'artwork_comment' : forms.Textarea(attrs={'class':'form-control'}),
        }