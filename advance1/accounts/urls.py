from django.urls import path
from . import views 

urlpatterns = [

    path('upload/', views.upload_profile, name="upload_profile"),
    path('profile/', views.view_profile, name="view_profile"),

    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
