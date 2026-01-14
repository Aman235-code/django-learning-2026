## Templates #1

### Basics and Variables

- you can display the value of a variable in html template using {{}}

```python
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
            "content": "<b>This is the content of my first blog post</b>.",
            "created_at": datetime(2025, 1, 15, 10, 30) # y, m, d, h, m
        },
        "empty_value": None
    }

    return render(request, 'blog/user_info.html', context)
```

- to use it in template 

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>#1 Template Basics</title>
</head>
<body>
    <h1>Template Basic - User Information</h1>
    <p>This is user information page.</p>
    <!-- this is a comment -->

    {% comment %} 
    another way 
    to write a comment 
    recommended
    {% endcomment %}

    {# single line comment #}

    {% comment %} Single Variable {% endcomment %}
    <p>Name: {{name}}</p>
    <p>Age: {{age}}</p>

    {% comment %} List Access {% endcomment %}
    <p>First Skill: {{skill.0}}</p>
    <p>Skills: {{skill}}</p>

    {% comment %} Object Attribute {% endcomment %}
    <p>User Name: {{user.name}}</p>
    <p>User Age: {{user.age}}</p>

    {% comment %} Dictionary {% endcomment %}
    <h2>Blog Info</h2>
    <p>Title: {{blog.title}}</p>
    <p>Content: {{blog.content}}</p>

    {% comment %} Safe Filter {% endcomment %}
    <p>Content: {{blog.content | safe}}</p>
    <p>Created At: {{blog.created_at}}</p>

    {% comment %} Default Value {% endcomment %}
    <p>Default Empty Value: {{ empty_value|default:"No value"}}</p>

    {% comment %} run only if None is provided{% endcomment %}
    <p>Default Empty Value: {{ empty_value|default_if_none:"No Data"}}</p>

    {% comment %} Nested Variable {% endcomment %}
    <p>Author: {{blog.author.name}}</p>
</body>
</html>
```

## Templates #2 

### Filters(Text, Numbers, Date)

```python

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
```

- template filters

```python
 <h1>Blog Filter Page</h1>

    {% comment  %} Text Filter {% endcomment %}
    <p><b>Title(Normal):</b> {{post.title}}</p>
    <p><b>Uppercase:</b> {{post.title|upper}}</p>
    <p><b>Lowercase:</b> {{post.title|lower}}</p>
    <p><b>Capitalize:</b> {{post.title|capfirst}}</p>
    <p><b>Title Case:</b> {{post.title|title}}</p>
    <p><b>Truncate Char:</b> {{post.title|truncatechars:20}}</p>
    <p><b>Truncate Words:</b> {{post.title|truncatewords:2}}</p>
    <p><b>Line Break:</b> {{post.title|linebreaks}}</p>

    <hr/>

    {% comment  %} Number Filter {% endcomment %}
    <p><b>Original Price:</b> {{post.price}}</p>
    <p><b>Original Price(+5):</b> {{post.price|add:5}}</p>

    {% if post.number|divisibleby:2 %}
    <p>{{post.number}} is Even</p>
    {% else %}
    <p>{{post.number}} is Odd</p>
    {% endif %}

    <hr/>

    {% comment  %} List Filter {% endcomment %}
    <p><b>Normal Tag:</b> {{post.tags}}</p>
    <p><b>First Tag:</b> {{post.tags|first}}</p>
    <p><b>Last Tag:</b> {{post.tags|last}}</p>
    <p><b>Length of Tags:</b> {{post.tags|length}}</p>
    <p><b>Slice (first 2):</b> {{post.tags|slice:":2"}}</p>
    <p><b>Join Tags:</b> {{post.tags|join:", "}}</p>

    <hr/>
    {% comment %} if author is having value -> yes, empty string -> no {% endcomment %}
    <p>Author Available?: {{post.author|yesno:"Yes,No,MayBe"}}</p>

    {% comment %} if comments > 1 it'll automatically add s to end {% endcomment %}
    <p>Commnets Count?: {{post.comments_count}} Comment{{post.comments_count|pluralize}}</p>
    
    <hr/>

    {% comment %} Date & Time filters{% endcomment %}
    <p><b>Created At:</b> {{post.created_at}}</p>
    <p><b>Formated Date (Date):</b> {{post.created_at|date:"D d M Y"}}</p>
    <p><b>Time Only (Time):</b> {{post.created_at|time:"H:i:s A"}}</p>

    {% comment  %} encoding & formatting {% endcomment %}
    <p><b>Title Encode:</b> {{post.title|urlencode}}</p>
    <p><b>Float Format:</b> {{123.4567891|floatformat:2}}</p>
```

## Templates #3

### Tags (Conrol flow)

```python

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
```

- template filters

```python
 <h1>Blog Tags Page</h1>
    <p>{{today}}</p>

    {% comment %} If Else {% endcomment %} {% if blog.0.is_featured %}
    <h2>Featured Blog: {{ blog.0.title }}</h2>
    {% else %}
    <h2>No Featured Blogs</h2>
    {% endif %} 
    
    
    {% comment %} For Loop {% endcomment %}
    <ul>
      {% for post in blog %}
      <li>
        {{forloop.counter}}. {{ post.title }} - {{ post.content }}
      </li>
      {% empty %}
      <li>No blog posts available.</li>
      {% endfor %}
    </ul>

    {% comment %} with {% endcomment %}
    {% with total_posts=blog|length %}
    <p>Total Blog Posts: {{ total_posts }}</p>
    {% endwith %}

    <hr/>

    {% comment %} cycle {% endcomment %}
    <h2>Blogs in Table</h2>
    <table border="1" cellpadding="5" cellspacing="0">
      <tr>
        <th>Title</th>
        <th>Content</th>
      </tr>
      {% for post in blog %}
      <tr style="background-color: {% cycle 'lightblue' 'lightgreen'  %} ">
        <td>{{ post.title }}</td>
        <td>{{ post.content }}</td>
      </tr>
      {% endfor %}
    </table>

    <hr/>
    {% comment %} FirstOf {% endcomment %}
    <p>Author: {% firstof blog.0.author "Anonymous" %}</p>

    <hr/>
    {% comment %} verbatim {% endcomment %}
    <h2>Verbatim Example</h2>
    {% verbatim %}
    <p>Author : {{blog.1.author}}</p>
    {% endverbatim %}

    {% comment %} autoescape {% endcomment %}
    <h2>Autoescape Example</h2>
    <p>Default(Safe escaped): {{html_code}}</p>
   


    {% autoescape off %}
    <p>{{ html_code }}</p>
    {% endautoescape %}

    {% comment %} or  {% endcomment %}
    {% comment %} <p>Default(Safe escaped): {{html_code|safe}}</p> {% endcomment %}
```

## Templates #4

### Inheritance & Staticn 

- template folder having reusable html code is created inside the root folder
- static folder(css, js, images) also created inside the root folder
- you need to register this in settings.py go to the last and add 

```python
STATICFILES_DIRS = [BASE_DIR / 'static']
```
- then we can load css, js, images in template usign load static
- you can import template from another template using include "template.html"
- base.html of root folder


```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %} My Django Project {% endblock %}</title>
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    {% include "navbar.html" %}
    <h1>welcome to my project</h1>
    <hr/>
    <div class="content">
    {% block content %} 
    {% endblock %}
    </div>

    <footer>
        <p>&copy; 2026 my site</p>
    </footer>

    <script src="{% static 'js/scripts.js' %}"></script>
   
</body>
</html>
```

- you can also use images after writing load static
- csrf - cross site request forgery used for security purpose to prevent xss attacks


```python
# home.html
{% extends 'base.html' %}
{% load static %}
{% block title %} Home - My Django Project {% endblock %}

{% block content %}
    <h2>Welcome to the Home Page</h2>
    <p>This is the home page of my Django project.</p>
    <img src="{% static 'images/logo.jpg' %}" alt="Home Image" />

    <form method="POST">
        {% csrf_token %}
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required placeholer="username"/>
        <input type="password" name="password" placeholder="password" />
        <button type="submit">Submit</button>
    </form>

    <button onclick="showAlert()">Click Me</button>

{% endblock %}
```

- for navbar routing you have change href attribute with url and write the name that you have written in name value of views.py file

```python
<nav>
    <ul>
        <li><a href="{% url 'blog-home' %}">Home</a></li>
        <li><a href="{% url 'blog-about' %}">About</a></li>
    </ul>
</nav>
```

## Templates #5

### Advanced & Rare Tags

- we have more tags just fir advance 

```python
  students_list = [
        {"name":"Alice", "class": "10th"},
        {"name":"Bob", "class": "9th"},
        {"name":"Charlie", "class": "8th"},
    ]
    return render(request, 'blog/blog.html', {"students": students_list})
```


```python
{% extends "base.html" %}

{% block title %} Blog Page {% endblock %}


{% block content %}
    <h1>Blog Us</h1>
    {% regroup students by class as grouped_students %}
    <ul>
        {% for group in grouped_students  %}
        <li>
            <strong>Class: {{ group.grouper }}</strong>
            <ul>
                {% for student in group.list %}
                <li>{{ student.name }}</li>
                {% endfor %}
            </ul>
        </li>
        {% endfor %}
    </ul>
    <p>
        {% comment %} 50/100 * 100  {% endcomment %}
        Progress : {% widthratio 50 100 100 %} %
    </p>
    {% spaceless %}
    <div>
        <h3>   This is    a    spaced   less    example.    </h3>
        <p>
            The    extra    spaces    in    this    div    will    be    removed.
        </p>
    </div>
    {% endspaceless %}

    {% comment %} block filter  {% endcomment %}
    {% filter upper %}
        this is converted to uppercase
    {% endfilter %}

    {% comment %} inline filter  {% endcomment %}
    {% for student in students %}
        <p>{{student.name|lower}} in class {{student.class|add:"+1"}}</p>
    {% endfor %}


{% endblock %}
```