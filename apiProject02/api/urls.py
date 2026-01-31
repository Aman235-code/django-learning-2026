from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('students/', StudentAPI.as_view()),
    path('students/<int:pk>',StudentAPI.as_view())
]
