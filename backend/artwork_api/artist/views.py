from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages
from django.views import generic
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from artwork.models import Profile
from .forms import ChangePasswordForm, SignupForm, EditProfileForm,CreateProfileForm

# Create your views here.
class CreateProfileView(generic.CreateView):
    model = Profile
    form_class = CreateProfileForm
    template_name = 'registration/create_profile.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def create_profile_action(request):
    userid = request.user.id
    if request.method == 'POST':
         
            profile_form = CreateProfileForm(request.POST)
            
            
            
            if profile_form.is_valid():
                newprof = profile_form.save(commit=False)
                newprof.profile_picture = request.FILES['newprofilepic'] 
                
                newprof.save()
           
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='explore')
            else:
                print(profile_form.errors.as_data())
                print("can't edit")       
    else:
            profile_form = CreateProfileForm

    

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
    form_class = ChangePasswordForm
    template_name='registration/password.html'
    success_url = reverse_lazy('explore')

def change_password(request):
    if request.method == 'POST':
        form = ChangePasswordForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('explore')
        else:
            print(user.id.old_password)
            print(form.errors.as_data())
            print("can't edit")   
    else:
        form = ChangePasswordForm(request.user)
    return render(request, 'registration/password.html', {
        'form': form
    })

def updateprofile(request, pkreq):
        userprofile = Profile.objects.get(pk=pkreq)
        
        if request.method == 'POST':
         
            profile_form = EditProfileForm(request.POST, instance=userprofile)
            updatecom = profile_form.save(commit=False)
            updatecom.user.pk = userprofile.pk
            
            if profile_form.is_valid():
                
                updatecom.profile_picture = request.FILES['newprofilepic']
                
                updatecom.save()
           
                messages.success(request, 'Your profile is updated successfully')
                return redirect(to='explore')
            else:
                print(profile_form.errors.as_data())
                print("can't edit")       
        else:
            profile_form = EditProfileForm(instance=userprofile)