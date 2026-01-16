from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('contact/', views.contact, name='contact'),
    path('submit/', views.submit_form, name='submit_form'),
]