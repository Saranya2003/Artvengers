from django.contrib.auth import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm,PasswordChangeForm, SetPasswordForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields
from artwork.models import Profile

class SignupForm(UserCreationForm):
    email = forms.EmailField(label="",widget=forms.EmailInput(attrs={'class': 'form-control rounded-pill','placeholder': 'Email'}))
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'class': 'form-control rounded-pill','placeholder': 'Username'}),help_text="")
    password1 = forms.CharField(label="",help_text="",max_length=20,widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill','type':'password','placeholder': 'Password'}))
    password2 = forms.CharField(label="",help_text="",max_length=20,widget=forms.PasswordInput(attrs={'class': 'form-control rounded-pill','type':'password','placeholder': 'Confirm Password'}))
    class Meta:
        model = User
        fields = ('email','username','password1','password2')


    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'user','email','Instagram','Twitter','Facebook'}
        field_order = ['user','email','Instagram','Twitter','Facebook']

class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = {'user','email','Instagram','Twitter','Facebook'}
        field_order = ['user','email','Instagram','Twitter','Facebook']


class ChangePasswordForm(SetPasswordForm):
    #old_password = forms.CharField(label="",help_text="",max_length=100,widget=forms.PasswordInput(attrs={'type':'hidden','value':'user.old_password','class':'form-control','is_hidden':'true'}))
    new_password1 = forms.CharField(label="",help_text="",max_length=100,widget=forms.PasswordInput(attrs={'type':'password','class':'form-control'}))
    new_password2 = forms.CharField(label="",help_text="",max_length=100,widget=forms.PasswordInput(attrs={'type':'password','class':'form-control'}))


    class Meta:
        model = User
        fields = ('new_password1','new_password2')