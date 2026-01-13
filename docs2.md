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