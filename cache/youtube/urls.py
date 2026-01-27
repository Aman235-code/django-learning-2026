from django.urls import path 
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('user-profile-list/', views.user_profile_list, name='user_profile_list')
]
