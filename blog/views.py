from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from .models import Category, Profile,Blog,Comment,Likes
from .forms import DetailsForm,AddBlogForm,CommentForm
from django.http  import HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib import messages
from blog.permissions import IsAdminOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializer import BlogSerializer

# Create your views here.
def welcome(request):
    blog=Blog.objects.all()
    current_user=request.user
    comments = Comment.get_comments()
    categories=Category.get_all_category()
    if request.method=='POST':

        form=CommentForm(request.POST,request.FILES)
       
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = current_user
            comment.blog = Blog.objects.get(id=int(request.POST["blog_id"]))
            comment.save()   
            return redirect('welcome')
    else:
           
            form=CommentForm
    return render(request,'welcome.html',{'form':form,'blogs':blog,'comments':comments, 'categories':categories})


@login_required(login_url='/accounts/login/')
def profile(request):

    # current_user=get_object_or_404(User,id=user_id)
    current_user = request.user
    blog = Blog.objects.filter(user=current_user)
    profile = Profile.objects.filter(user = current_user).first()
    form=AddBlogForm()
    
    return render(request, 'profile.html', {"blog": blog,'form':form, "profile": profile})

def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
                Profile.objects.filter(id=current_user.profile.id).update(bio=form.cleaned_data["bio"])
                profile = Profile.objects.filter(id=current_user.profile.id).first()
                # profile.profile_photo.delete()
                profile.profile_photo=form.cleaned_data["profile_photo"]
                profile.save()
        return redirect('profile')

    else:
        form = DetailsForm()
    
    return render(request, 'edit_profile.html',{"form": form})



@login_required
def search_blog(request):
    """
    Function that searches for projects
    """
    if 'blog' in request.GET and request.GET["blog"]:
        search_term = request.GET.get("business")
        searched_blog = Blog.objects.filter(name__icontains=search_term)
        message = f"{search_term}"
        blog = Blog.objects.all()
        
        return render(request, 'search.html', {"message": message, "businesses": searched_blog})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

@login_required(login_url='/accounts/login/')
def add_blog(request):
    if request.method == "POST":
        form = AddBlogForm(request.POST, request.FILES)
        if form.is_valid():
            blog = form.save(commit=False)
            form.instance.user = request.user
            blog.save()
        return redirect('welcome')
    else:
        form = AddBlogForm()
    return render(request, 'add_blog.html', {"form": form})

@login_required(login_url='/accounts/login/')
def blog_details(request, blog_id):
  
  try:
    blog_details = Blog.objects.get(pk = blog_id)
  
  except Blog.DoesNotExist:
    raise Http404
  
  return render(request, 'blog_details.html', {"details":blog_details})



class BlogList(APIView):
    def get(self, request, format=None):
        all_blogs = Blog.objects.all()
        serializers = BlogSerializer(all_blogs, many=True)
        permission_classes = (IsAdminOrReadOnly,)
        return Response(serializers.data)  

def like_blog(request, blog_id):
    blog = get_object_or_404(Blog,id = blog_id)
    like = Likes.objects.filter(blog = blog ,user = request.user).first()
    if like is None:
        like = Likes()
        like.blog = blog
        like.user = request.user
        like.save()
    else:
        like.delete()
    return redirect('welcome')  

def get_category(request,category_id):
    blog =Blog.filter_by_category(category_id)
    

    return render (request,'category.html',{'blog':blog})





