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

# Template #1
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

# Template #2
def blog_details(request):

    post = {
        "title": "Understanding Django Views",
        "description": "A comprehensive guide to Django views.",
        "author": None,
        "content": "This post explains how Django views work in detail.",
        "created_at": datetime(2024, 5, 20, 14, 0),
        "comments_count": 5,
        "tags": ["Django", "Web Development", "Python"],
        "price": 100,
        "number": 7
    }

    return render(request, 'blog/blog_details.html', {"post": post})

# Template #3

def blog_list(request):
    blogs = [
        {"title": "Django Basics","is_featured":True, "author": "Alice", "content": "An introduction to Django."},
        {"title": "Advanced Django","is_featured":False, "author": "Bob", "content": "Deep dive into Django features."},
        {"title": "Django Templates","is_featured":False, "author": "Charlie", "content": "Understanding Django templating system."},
    ]
    context = {
        "blog":blogs,
        "today": datetime.now(),
        "html_code": "<h1>This is a heading</h1><p>This is a paragraph.</p>"
    }
    return render(request, 'blog/blog_list.html', context)