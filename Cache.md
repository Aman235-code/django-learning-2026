## In-Memory Cache (LocMemCache)

- very fast
- best for dev/small apps
- cleared on process start

- settings.py at the last

```python
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
```

- usage 

```python
def user_list(request):
    users = cache.get('users_data') # any name
    if not users:
        print("Fetching from DB")
        users = YoutubeUser.objects.all()
        cache.set('users_data', users, timeout=300)  # Cache for 5 min 60*5
    else:
        print("Fetching from Cache")
    return render(request, 'user_list.html', {'users': users})
```

- if you want to clear cache

```python
#admin.py
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
```

