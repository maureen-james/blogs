from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from .models import Profile,Blog
from .forms import DetailsForm,BlogPostForm,AddBlogForm
from django.http  import HttpResponse,Http404

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

@login_required(login_url='/accounts/login/')
def profile(request):
    # posts=Post.objects.all()
    current_user = request.user

    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES)
        form1 = BlogPostForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        if form1.is_valid():
            post = form1.save(commit=False)
            post.profile = current_user.profile
            post.save()

        return redirect('profile')

    else:
        form = DetailsForm()
        form1 = BlogPostForm()
    
    return render(request, 'profile.html', {"form":form,"form1":form1})

@login_required(login_url='/accounts/login/')
def edit_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = DetailsForm(request.POST, request.FILES)
        if form.is_valid():
                Profile.objects.filter(id=current_user.profile.id).update(bio=form.cleaned_data["bio"])
                profile = Profile.objects.filter(id=current_user.profile.id).first()
                profile.profile_pic.delete()
                profile.profile_pic=form.cleaned_data["profile_pic"]
                profile.save()
        return redirect('profile')

    else:
        form = DetailsForm()
    
    return render(request, 'edit_profile.html',{"form": form}) 


@login_required
def search_business(request):
    """
    Function that searches for projects
    """
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        # searched_business = Business.objects.filter(name__icontains=search_term)
        message = f"{search_term}"
        # businesses = Business.objects.all()
        
        return render(request, 'search.html', {"message": message})

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
        form = BlogPostForm()
    return render(request, 'add_blog.html', {"form": form})

@login_required(login_url='/accounts/login/')
def blog_details(request, blog_id):
  
  
  try:
    project_details = Blog.objects.get(pk = blog_id)
  
  except Blog.DoesNotExist:
    raise Http404
  
  return render(request, 'blog_details.html', {"details":project_details})



