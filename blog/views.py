from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from .models import Profile,Blog
from .forms import DetailsForm,AddBlogForm
from django.http  import HttpResponse,Http404
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def welcome(request):
    blog=Blog.objects.all()
    if request.method=='POST':
        current_user=request.user
        form=AddBlogForm(request.POST,request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.user=current_user
            blog.save()
            messages.success(request,('blog was posted successfully!'))
            return redirect('welcome')
    else:
            form=AddBlogForm()
    return render(request,'welcome.html',{'form':form,'blog':blog})

    # return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def profile(request):

    # current_user=get_object_or_404(User,id=user_id)
    current_user = request.user
    blog = Blog.objects.filter(user=current_user)
    profile = Profile.objects.filter(id = current_user.id).first()
    form=AddBlogForm()
    
    return render(request, 'profile.html', {"blog": blog,'form':form, "profile": profile})




# @login_required(login_url='/accounts/login/')
# def edit_profile(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = DetailsForm(request.POST, request.FILES)
#         if form.is_valid():
#                 Profile.objects.filter(id=current_user.profile.id).update(bio=form.cleaned_data["bio"])
#                 profile = Profile.objects.filter(id=current_user.profile.id).first()
#                 profile.profile_pic.delete()
#                 profile.profile_pic=form.cleaned_data["profile_pic"]
#                 profile.save()
#         return redirect('profile')

#     else:
#         form = DetailsForm()
    
#     return render(request, 'edit_profile.html',{"form": form}) 
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
                Profile.objects.filter(id=current_user.profile.id).update(bio=form.cleaned_data["bio"])
                profile = Profile.objects.filter(id=current_user.profile.id).first()
                profile.profile_photo.delete()
                profile.profile_photo=form.cleaned_data["profile_photo"]

                profile.save()
        return redirect('profile')

    else:
        form = DetailsForm()
    
    return render(request, 'update_profile.html',{"form": form})



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
            project = form.save(commit=False)
            form.instance.user = request.user
            project.save()
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



