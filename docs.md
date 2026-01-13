## Django

- high level python web framework
- designed for fast, secure, scalable development
- open source & community-driven
- follows MVT(Model-View-Template) architecture
- Motto: Web framework for perfectionists with deadlines

## Key features

- Batteries Included - Built-in tools for authentication, admin panel, ORM etc
- Scalable - from small apps to large-scale platforms
- Secure - protects against SQL injection, XSS, CSRF
- Cross platform - Works on Windows, Mac, Linux
- Strong Community Support - Large ecosystem of plugins and tutorials

## Why Use Django?

- Fast development = Build projects quickly
- Security - Inbuilt security
- Scalability - handles high traffic and large datasets
- Built=in admin panel - Manage data without coding
- Reusable Code - Write once, use multiple times

## Real World Use

- Instagram - Social Media
- Pinterest - Image sharing platform
- Mozilla - Add-ons Store

## MVT Workflow in Django

- User sends a request(URL)
- URL dispatcher maps req to the view
- View interacts with model to get/save data
- View sends data to template
- Template renders HTML
- HTML sent as response to user

## MVT vs MVC

- MVT is a variation of MVC
- MVC -> Controller = Django's view
- MVT -> template handles presentation layer
- Terminology changes, core concept is same

## Installing Python & Django

- python --version (Python 3.14.0)
- pip --version
- pip install django (if you dont have django installed)
- django-admin --version (if you have django installed)
- pip install virtualenv
- virtualenv myenv (any name)
- myenv\Scripts\activate (activate)

## Create Django Project

- pip install django (if you dont have django installed)
- django-admin --version (if you have django installed)
- django-admin startproject myProject (any name)
- cd myProject
- python manage.py runserver (default 8000)
- python manage.py runserver 8080 -> to run on port 8080

- python manage.py startapp blog (create app inside my Project)

## Django Project Structure

- Outer Folder (root folder)
  manage.py

- Inner folder
  settings.py -> configuarations (apps, db. tamplates, static, timezone)
  urls.py -> route URLs to views
  asgi.py -> async gateway interface (entry point) -> Modern Deployment
  wsgi.py -> web server gateway interface -> Production Deployment
  **init**.py -> starting point

## Create first view in your app

- one project can have multiple apps
- go to cd myProject ( folder having main project)
- python manage.py startapp blog(app name)

- migrations -> database related
- admin.py -> admin panel config settings
- apps.py -> app config details 
- models.py -> db models(tables)
- tests.py -> unit testing 
- views.py -> class, func

- in settings.py of main project you need to regsiter app name (INSTALLED APPS)


- 1. Function views
-    1. Add an import:  from my_app import views
-    2. Add a URL to urlpatterns:  path('', views.home, name='home')

- goto views.py of blog folder

```python
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("Welcome to the blog home page")
```

- then goto main project's url file

```python
from django.contrib import admin
from django.urls import path
from blog.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', home, name="home"),
]
```

- or in this way too

```python
from django.contrib import admin
from django.urls import path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', views.home, name="home"),
]
```

- goto settings.py of main project
- in line 33 INSTALLED APPS add your app name(blog) at the last to register your app

- then run the server
- go to http://127.0.0.1:8000/blog/ and you'll see the output

- Including another URLconf
-   1. Import the include() function: from django.urls import include, path
-   2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

- create a file urls.py in your blog folder

```python
from django.urls import path
from blog import views # or from . import views because you're in same folder

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about")
]
```

- in main projects urls file

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls'))
]
```

- then you can directly see about's in http://127.0.0.1:8000/about/ link

- you can create multiple apps in a single project like blog or shop
- make sure to add urls.py in apps folders and also views.py 
- then you have to register your app name in settings.py installed apps
- after that you have to change in urls.py of the main project 

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('shop/', include('shop.urls'))
]
```

## URL Parameters (path, re_path, kwars)

### path

- if you have paramter in views 

```python
def post_details(request, post_id): # post_id is int
    return HttpResponse(f"<h1>Details of post {post_id}</h1>")

def user_profile(request, username): # username is string
    return HttpResponse(f"<h1>Profile of user {username}</h1>")
```

- you can define it in urls file using

```python
path('post/<int:post_id>/', views.post_details, name="post_details"),
path('user/<str:username>/', views.user_profile, name="user_profile"),
```

- name of parameters should match with path (user/<str:username> -> username)

- then you can test dynamic route using

```python
http://127.0.0.1:8000/blog/post/2/ 
http://127.0.0.1:8000/blog/user/aman/
```

## repath

- related to regex (search feature)
- helpful in complex patterns
- you have to import in in urls.py using 

```python
# urls.py
from django.urls import path, re_path
```

- in urlPatters you can search for a specific year using regex

```python
re_path(r'^article/(?P<year>[0-9]{4})/$', views.article_by_year, name="article_by_year"),
```

- views.py

```python
def article_by_year(request, year):
    return HttpResponse(f"<h1>Articles from the year {year}</h1>")
```

- then you can get 2026 article using

```python
http://127.0.0.1:8000/blog/article/2026/
```

## kwargs 

- kwargs stands for keyword arguments

```python
def article_details(request, year, month):
    return HttpResponse(f"<h1>Articles: from {year} - {month}</h1>")

def article_details(request, **kwargs):
    return HttpResponse(f"<h1>Articles from {kwargs['year']} - {kwargs['month']} - {kwargs['day']}</h1>")
```

- urls file (here you can add day too without changing that function)

```python
path('article/<int:year>/<int:month>/<int:day>', views.article_details, name="article_details"),
```

- then you can directly use both year and month

```python
http://127.0.0.1:8000/blog/article/2026/4/30
```


