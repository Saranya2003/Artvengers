from typing import Any, Dict
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from artwork.models import Profile
from .forms import PasswordChangeForm, SignupForm, EditProfileForm

# Create your views here.
class UserRegisterView(generic.CreateView):
    form_class = SignupForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

class UpdateProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('explore')

    def get_object(self):
        return self.request.user
    
class ShowProfileView(generic.DetailView):
     model = Profile
     template_name = 'registration/profile.html'

     def get_context_data(self,*args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfileView, self).get_context_data(*args,**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
     

class ChangePasswordsView(PasswordChangeView):
    form_class = PasswordChangeForm
    template_name='registration/password.html'
    success_url = reverse_lazy('dashboard')

def updateprofile(request, pkreq):
        userprofile = Profile.objects.get(pk=pkreq)
        
        if request.method == 'POST':
         
            profile_form = EditProfileForm(request.POST, instance=userprofile)
            updatecom = profile_form.save(commit=False)
            updatecom.user.pk = userprofile.pk
            if profile_form.is_valid():
                
                
                updatecom.save()
           
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='explore')
            else:
                print(profile_form.errors.as_data())
                print("can't edit")       
        else:
            profile_form = EditProfileForm(instance=userprofile)