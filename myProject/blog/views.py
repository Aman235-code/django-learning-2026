from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

# Create your views here.
def home(request):
    return HttpResponse("<h1>Blog Home page</h1>")

def about(request):
    return HttpResponse("<h1>Blog About page</h1>")

def post_details(request, post_id):
    return HttpResponse(f"<h1>Details of post {post_id}</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>Profile of user {username}</h1>")

def article_by_year(request, year):
    return HttpResponse(f"<h1>Articles from the year {year}</h1>")

# def article_details(request, year, month):
#     return HttpResponse(f"<h1>Articles: from {year} - {month}</h1>")

def article_details(request, **kwargs):
    return HttpResponse(f"<h1>Articles from {kwargs}</h1>")

def post_list(request):
    return render(request, 'blog/post_list.html')

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def user_info(request):

    context = {
        "name": "Alice",
        "age": 30,
        "skill": ["Django", "Python", "JavaScript"],
        "user": User("Bob", 25),
        "blog": {
            "title": "My First Blog",
            "author": {
                "name": "Charlie",   
            },
            "content": "<b>This is the content of my first blog post</b>.",
            "created_at": datetime(2025, 1, 15, 10, 30) # y, m, d, h, m
        },
        "empty_value": None
    }

    return render(request, 'blog/user_info.html', context)