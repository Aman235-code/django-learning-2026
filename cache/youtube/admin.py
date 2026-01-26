from django.contrib import admin
from .models import YoutubeUser
from django.core.cache import cache
from django.contrib import messages

@admin.action(description='Clear User Cache')
def clear_user_cache(modeladmin, request, queryset):
    cache.delete('users_data')
    messages.success(request, "User cache cleared successfully.")

# Register your models here.
@admin.register(YoutubeUser)
class YoutubeUserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subscribers')

    actions = [clear_user_cache]