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