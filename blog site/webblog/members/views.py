from typing import Any
from django.db import models
from django.shortcuts import render,redirect, get_object_or_404
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from .forms import LoginForm, SignupForm, EditProfileForm, PasswordChangingForm, CreateProfileForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView
from blogapp.models import Profile


# Create your views here.

class UserRegistrationView(generic.CreateView):
    form_class = SignupForm
    template_name = 'members/register.html'
    success_url = reverse_lazy('login')
    
class UserEditProfileView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'members/edit_profile.html'
    success_url = reverse_lazy('home')
    
    def get_object(self):
        return self.request.user
    
class PasswordChangingView(PasswordChangeView):
    form_class = PasswordChangingForm
    template_name = 'members/password_change.html'
    success_url = reverse_lazy('password_sucess')
    
class ShowProfilePageView(generic.DetailView):
    model = Profile
    template_name = 'members/profile_page.html'
    
    def get_context_data(self, *args, **kwargs):
        #cat_menu = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context
    
class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'members/edit_profile_page.html'
    fields = ['bio','profile_pic','facebook_url', 'twitter_url', 'instagram_url', 'pintrest_url']
    success_url = reverse_lazy('home')
    
class CreateProfilePageView(generic.CreateView):
    model = Profile
    template_name = 'members/create_profile_page.html'
    form_class = CreateProfileForm
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    
def success(request):
    return render(request, 'members/success.html')

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'members/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
