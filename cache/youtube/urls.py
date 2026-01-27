from django.urls import path 
from . import views

urlpatterns = [
    path('users/', views.user_list, name='user_list'),
    path('users-two/', views.user_two, name='user_two'),
    path('user-profile-list/', views.user_profile_list, name='user_profile_list'),
    path('clear/', views.clear_cache, name='clear_cache'),
    path('users-db/', views.user_db_list, name='user_db_list'),
]
