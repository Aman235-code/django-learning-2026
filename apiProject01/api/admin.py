from django.contrib import admin
from .models import Student, Student2
# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display= ('id', 'name', 'age', 'city')

@admin.register(Student2)
class StudentAdmin2(admin.ModelAdmin):
    list_display= ('id', 'name', 'age', 'email')