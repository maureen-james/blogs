from .models import Profile
from django import forms

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

# class PostForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ['profile','date','like']