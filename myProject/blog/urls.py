from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.home, name="blog-home"),
    path('about/', views.about, name="blog_about"),
    path('post/<int:post_id>/', views.post_details, name="post_details"),
    path('user/<str:username>/', views.user_profile, name="user_profile"),
    re_path(r'^article/(?P<year>[0-9]{4})/$', views.article_by_year, name="article_by_year"),
    path('article/<int:year>/<int:month>/<int:day>', views.article_details, name="article_details"),

    path('posts/', views.post_list, name="post_list"),

    path('user-info/', views.user_info, name="user_info"),
    path('blog-details/', views.blog_details, name="blog_details"),
    path('blog-list/', views.blog_list, name="blog_list"),
]