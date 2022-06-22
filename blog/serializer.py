from rest_framework import serializers
from .models import Blog
# class ProfileSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Profile
#         fields = ('profile_photo', 'bio', 'user')

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ('title', 'image', 'content', 'posted_date', 'user',)        