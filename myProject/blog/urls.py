from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog_about"),
    path('post/<int:post_id>/', views.post_details, name="post_details"),
    path('user/<str:username>/', views.user_profile, name="user_profile"),
]