from .models import Profile,Blog
from django import forms

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ['profile','date','like']