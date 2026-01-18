from django.urls import path 
from . import views 

urlpatterns = [
    path('add/', views.student_create, name='student_create'),
    path('', views.student_list, name='student_list'),
    path('details/<int:pk>/', views.student_detail, name='student_detail'),
    path('edit/<int:pk>/', views.student_update, name='student_update'),
    path('delete/<int:pk>/', views.student_delete, name='student_delete'),
    path('show-msg/', views.show_message, name='show_message'),
]
