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
]