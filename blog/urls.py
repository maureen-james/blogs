from django.urls import path, re_path as url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns=[
    path('',views.welcome,name = 'welcome'),
    path('profile/',views.profile,name = 'profile'),
    path('search/', views.search_blog, name='search'),
    path('user/', views.profile, name='profile'),
    path('user/edit_profile/', views.edit_profile, name='edit_profile'),
    path('profile/addblog/', views.add_blog, name='add_blog'),
    path('blogdetails/<blog_id>',views.blog_details,name='blogdetails'),
   


]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
        