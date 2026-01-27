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

## File Based Cache

- settings.py at last

```python
CACHES = {
    'default': {
        # file based cache
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'my_cache', # secify cache directory
        'TIMEOUT': 300, # 300 seconds -> 5 min
        'OPTIONS': {
            'MAX_ENTRIES': 1000 # max no of entries in cache
        }
    }
}
```

```python

class UserProfile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    sub = models.IntegerField(default=0)

    def __str__(self):
        return self.name
```


```python
from django.shortcuts import render
from .models import YoutubeUser, UserProfile, UserList
from django.core.cache import cache

def user_profile_list(request):
    users_data = cache.get('users_data')

    if users_data is None:
        print('Fecthing data from database')
        users_data = UserProfile.objects().all()
        cache.set('users_data', users_data)
    
    else:
         print('Fecthing data from cache')
    return render(request, 'user_profile_list.html',{ 'users': users_data})
```

## Per View Cache

- settings.py

```python
CACHES = {
    'default': {
        # per view cache
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': BASE_DIR / 'file_cache', # secify cache directory
    }
}
```

- views.py

```python
from django.shortcuts import render
from .models import YoutubeUser, UserProfile, UserList
from django.core.cache import cache
from django.views.decorators.cache import cache_page


@cache_page(30) # cache this view for 30 sec
def user_two(request):
    print('Fecthing data from database')
    users = UserList.objects.all()
    return render(request, 'users.html', {'users': users})
```

