from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save

import blog

# Create your models here.
# class category
# class location
# class profile
# class post

class Blog(models.Model):
    """
    This class takes care of the posted projects
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projects')
    image = CloudinaryField('image')
    title = models.CharField(max_length=50)
    description =  models.TextField(max_length=255,  null=True)
    category=models.ForeignKey('Category',on_delete=models.CASCADE,null=True)
    url = models.TextField(null=True)
    content=models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True)
    

    @classmethod
    def get_blog_by_user(cls, user):
        blog = cls.objects.filter(user=user)
        return blog

    def save_blog(self):
        self.save()

    def delete_blog(self):
        self.delete()

    #  get by id
    @classmethod
    def get_one_blog(cls, id):
        blog = cls.objects.get(id=id)
        return blog

    
    @classmethod
    def search_by_title(self, search_title):
        
        blog = Blog.objects.filter(title__icontains=search_title)
        return blog

    # get images by category
    @classmethod
    def filter_by_category(cls, category_id):
        blog = Blog.objects.filter(category_id=category_id)
        return blog 
  

    def __str__(self):
        return self.user.username  


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_photo = CloudinaryField('image')

    bio = models.TextField(max_length=500, blank=True, null=True)

    email =models.EmailField(max_length=60, blank=True)


    contact = models.CharField(max_length=50, blank=True, null=True)

    def update(self):
        self.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile_by_user(cls, user):
        profile = cls.objects.filter(user=user)
        return profile       
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    @classmethod
    def search_profiles(cls, search_term):
        profiles = cls.objects.filter(user__username__icontains=search_term).all()
        return profiles 

class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog, on_delete=models.CASCADE,null=True)
    comment=models.CharField(max_length=255)
    posted=models.DateTimeField(auto_now_add=True) 

    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments

    def save_comment(self):
        self.save()        

class Likes(models.Model):
    blog = models.ForeignKey(Blog,related_name='like_count', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.blog
    def save_likes(self):
        self.save()

    # update like
    def update_likes(self, name):
        self.name = name
        self.save()

     # delete like from database
    def delete_likes(self):
        self.delete()

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    @classmethod
    def get_all_category(cls):
        categories = Category.objects.all()
        return categories
    def __str__(self):
        return self.name
    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

    @classmethod
    def update_category(cls,id,name):
        cls.objects.filter(id = id).update(name = name)       