from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from blogapp.models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    
    
    
    
class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        
        def __init__(self, *args, **kwargs):
            super(SignupForm, self).__init__()
            
            self.fields["username"].widget.attrs.update({"class": "form-control"})
            self.fields["password1"].widget.attrs.update({"class": "form-control"})
            self.fields["password2"].widget.attrs.update({"class": "form-control"})
           # self.fields['username'].widget.attrs['class'] = 'form-control'
           # self.fields['password1'].widget.attrs['class'] = 'form-control'
           # self.fields['password2'].widget.attrs['class'] = 'form-control'
        
class EditProfileForm(UserChangeForm):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))   
    first_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    last_login = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    is_superuser = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_staff = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    is_active = forms.CharField(max_length=200, widget=forms.CheckboxInput(attrs={'class':'form-check'}))
    date_joined = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'last_login', 'is_staff','is_active', 'date_joined']
        
        
class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password1 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    new_password2 = forms.CharField(max_length=200, widget=forms.PasswordInput(attrs={'class':'form-control', 'type':'password'}))
    
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        
        
class CreateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio','profile_pic','facebook_url', 'twitter_url', 'instagram_url', 'pintrest_url']
        
        widgets = {
            'bio' : forms.Textarea(attrs={'class':'form-control'}),
            'facebook_url' : forms.TextInput(attrs={'class':'form-control'}),
            'twitter_url' : forms.TextInput(attrs={'class':'form-control'}),
            'instagram_url' : forms.TextInput(attrs={'class':'form-control'}),
            'pintrest_url' : forms.TextInput(attrs={'class':'form-control'}),
        }