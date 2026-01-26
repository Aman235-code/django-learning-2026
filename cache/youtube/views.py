from django.shortcuts import render
from .models import YoutubeUser
from django.core.cache import cache

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