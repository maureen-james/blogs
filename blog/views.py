from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render,redirect
from .models import Profile,Blog
from .forms import DetailsForm,BlogPostForm

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

