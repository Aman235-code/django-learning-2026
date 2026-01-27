from django.shortcuts import render
from .models import YoutubeUser, UserProfile, UserList
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.http import HttpResponse

# Create your views here.
def user_list(request):
    users = cache.get('users_data')
    if not users:
        print("Fetching from DB")
        users = YoutubeUser.objects.all()
        cache.set('users_data', users, timeout=300)  # Cache for 5
    else:
        print("Fetching from Cache")
    return render(request, 'user_list.html', {'users': users})

def user_profile_list(request):
    users_data = cache.get('users_data')

    if users_data is None:
        print('Fecthing data from database')
        users_data = UserProfile.objects.all()
        cache.set('users_data', users_data)
    
    else:
         print('Fecthing data from cache')
    return render(request, 'user_profile_list.html',{ 'users': users_data})

@cache_page(30) # cache this view for 30 sec
def user_two(request):
    print('Fecthing data from database')
    users = UserList.objects.all()
    return render(request, 'users.html', {'users': users})

def clear_cache(request):
    cache.clear()
    return HttpResponse("Cache Cleared")