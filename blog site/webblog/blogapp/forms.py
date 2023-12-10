from django import forms
from .models import Post, Category, Comment

choices = Category.objects.all().values_list('name','name')

choices_list = []

for items in choices:
    choices_list.append(items)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','title_tag','category','author','body','snippet','header_image']
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control','value':'', 'id':'user', 'type':'hidden'}),
            #'author' : forms.Select(attrs={'class':'form-control'}),
            'category' : forms.Select(choices=choices_list,attrs={'class':'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }
        
        
        
class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','title_tag','body','snippet']
        
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'title_tag' : forms.TextInput(attrs={'class':'form-control'}),
            #'author' : forms.Select(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
            'snippet' : forms.Textarea(attrs={'class':'form-control'}),
        }

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name','body']
        
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'body' : forms.Textarea(attrs={'class':'form-control'}),
        }