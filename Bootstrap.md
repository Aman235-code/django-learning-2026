## Bootstrap in Django

- you can create virtual env in your root project folder too
- just go to that root directory (cd bootstrap)
- python -m venv venv
- venv\Scripts\activate

- you can install bootstrap in 3 ways

- 1st way
- using CDN (fast method but requires internet and slow load when it's slow)
- you have 2 links on docs copy those and paste them in root template base.html
- paste it above load static, link tag -> in base.html, script tag -> before ending body
- then you can see the result

- 2nd way
- downloading it -> in home page you see download link and it'll download zip file
- unzip it and goto css folder and copy bootstrap.min file
- paste it in root folder static/css file
- go to js folder & copy bootstrap.bundle.min file and paste it in root's folder static/js file
- no internet dependency, we can customize the css/js file
- we have to download again and again when ther's new version
- below load static paste 
-  <link rel="stylesheet" href="{% static 'css/bootstrap.min.css' %}">
-  <script src="{% static 'js/bootstrap.bundle.min.js' %}"></script>

- 3rd way
- using pip install bootstrap
- pip install django-bootstrap5
- in installed apps of settings.py file 

```python
  'django_bootstrap5',
  'blog',
```

- then above load static paste

```python
{% load django_bootstrap5 %}
{% bootstrap_css %}
{% bootstrap_javascript %}
```