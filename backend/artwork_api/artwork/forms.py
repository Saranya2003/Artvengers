from django import forms
from .models import ArtworkPost

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = ArtworkPost
        fields = {'Title','artistName','Description','Tag','Artwork'}
        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
            'artistName': forms.Select(attrs={'class':'form-control'}),
            'Description': forms.Textarea(attrs={'class':'form-control'}),
            'Tag': forms.TextInput(attrs={'class':'form-control'}),
        }