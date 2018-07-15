from django import forms
from .models import Newsfeed
from ckeditor.fields import RichTextField

class NewsfeedForm(forms.ModelForm):
    class Meta:
        model = Newsfeed
        fields = ['title', 'content', 'image', 'author']
        exclude = ['author']
    
        