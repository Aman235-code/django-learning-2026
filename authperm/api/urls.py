from django.urls import path 
from . import views 

# Basic Authentication + AllowAny & IsAuthenticated

# urlpatterns = [
#     path('public/', views.public_view, name='public_view'),
#     path('private/', views.private_view, name='private_view'),
# ]

# Session Authentication + IsAuthenticatedOrReadOnly

# urlpatterns = [
#     path('blogs/', views.blog_list, name='blog_list'),
# ]

# Token Authentication + IsAdminUser
from rest_framework.authtoken.views import obtain_auth_token # type: ignore

urlpatterns = [
    path('auth-token/', obtain_auth_token, name='api_token_auth'),
    path('profile/', views.user_profile, name='user_profile'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
]
