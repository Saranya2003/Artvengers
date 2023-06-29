from django.shortcuts import render, redirect
from django.contrib import messages
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from .forms import EditProfileForm,PasswordChangeForm, SignupForm

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UpdateProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('dashboard')

    
        
    def get_object(self):
        return self.request.user

class ChangePasswordsView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='registration/password.html'
    success_url = reverse_lazy('dashboard')

def updateprofile(request):
        if request.method == 'POST':
         
            profile_form = EditProfileForm(request.POST, instance=request.user.profile)

            if profile_form.is_valid() and profile_form.is_valid():
                profile_form.save()
           
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='users-profile')
        else:
            profile_form = EditProfileForm(instance=request.user)