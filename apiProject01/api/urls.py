from django.urls import path
from . import views 

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
    path('get-students/', views.get_students, name='get_students'),
    path('students/add', views.add_student, name="add_student"),
]
