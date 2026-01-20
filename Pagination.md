## Django Pagination

- after creating model in models.py make cahanes in admin.py to see the post db in admin panel
- add dummy data in admin panel to post
- uhrls  file

```python
urlpatterns = [
    path('', views.post_list, name='post_list'),
]
```

- views file

```python
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator

# Create your views here.
def post_list(request):
    post = Post.objects.all().order_by('id')
    paginator = Paginator(post, 4) # show 4 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})
```

- template

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pagination</title>
    <style>
        .pagination {
            display: flex;
            justify-content: center;
            margin-top: 20px
        }

        .pagination a, .pagination span {
            margin: 0 5px;
        }

        .pagination .a:hover{
            background-color: #f0f0f0
        }

        .pagination .current {
            background-color: #333
            color: white;
            border: 1px solid #333
        }
    </style>
</head>
<body>
    <h1>Blog Post</h1>
    <ul>
        {% for post in page_obj %}
            <li><b>{{post.title}}</b> - {{post.content}}</li>
        {% endfor %}
    </ul>

    {% comment %} pagination  {% endcomment %}
    <div class="pagination">
        {% if page_obj.has_previous %}
            <a href="?page=1">First</a>
            <a href="?page={{ page_obj.previous_page_number }}">Previous</a>
        {% endif %}

        {% for num in page_obj.paginator.page_range %}
            {% if page_obj.number == num %}
                <span class="current">{{num}}</span>
            {% else %}
                <a href="?page={{ num }}">{{num}}</a>
            {% endif %}
        {% endfor %}

        {% if page_obj.has_next %}
            <a href="?page={{ page_obj.next_page_number }}">Next</a>
            <a href="?page={{ page_obj.paginator.num_pages }}">Last</a>
        {% endif %}
    </div>
</body>
</html>
```