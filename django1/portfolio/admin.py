from django.contrib import admin
from portfolio.models import Student, Profile

# Register your models here.
# admin.site.register(Student)
# admin.site.register(Profile)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age','city') # displayed to user
    search_fields = ('name', 'city')
    list_filter = ('city',)
    ordering = ('name',)