from .models import Profile,Blog,Comment
from django import forms

class DetailsForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

# class BlogPostForm(forms.ModelForm):
#     class Meta:
#         model = Blog
#         exclude = ['profile','date','like']

class AddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','category','content','description','image','url']
            
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)            