from django.contrib.auth import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm,PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.forms import fields


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))


    class Meta:
        model = User
        fields = ('username','email','password1','password2')


    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)


        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'


class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput())


    class Meta:
        model = User
        fields = ('username','password')


class ChangePasswordForm(PasswordChangeForm):
    new_password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'type':'password'}))
    new_password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'type':'password'}))


    class Meta:
        model = User
        fields = ('new_password1','new_password2')