from django import forms
from .models import ArtworkPost

class ArtworkForm(forms.ModelForm):
    class Meta:
        model = ArtworkPost
        fields = {'Title','Description','Tag','Artwork'}
        widgets = {
            'Title': forms.TextInput(attrs={'class':'form-control'}),
        }