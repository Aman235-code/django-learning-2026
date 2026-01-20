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

## Search & Filters

- you can search using Q object

```python
from django.shortcuts import render
from .models import Post, MainBlog
from django.core.paginator import Paginator
from django.db.models import Q


def post_list1(request):
    query = request.GET.get('q') # search keyword
    category = request.GET.get('category') # category filter

    posts = MainBlog.objects.all()

    # Search using Q object
    if query:
        posts = posts.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) 
        )

    # filter by category
    if category:
        posts = posts.filter(category__iexact=category)

    return render(request, 'blog/post_res.html', {'posts': posts, 'query': query, 'category': category})
```

- template you can render as 

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Post Result Search & Filter</title>

</head>
<body>
    <h1>Search & Filter Exmaple</h1>

    <form method="GET" class="search-form">
        <input type="text" name="q" placeholder="Search..." value={{ query }}>
      

        <select name="category">
            <option value="">All Categories</option>
            <option value="Tech" {% if category == "Tech" %} selected{% endif %}>Tech</option>
            <option value="News" {% if category == "News" %} selected{% endif %}>News</option>
            <option value="Tutorial" {% if category == "Tutorial" %} selected{% endif %}>Tutorial</option>
        </select>

          <button type="submit">Search</button>
    </form>

    <ul>
        {% for post in posts %}
        <li>
            <h2>{{post.title}}</h2>
            <p>{{post.content}}</p>
            <p><strong>Category:</strong> {{post.category}}</p>
        </li>
        {% empty %}
            <li>No posts found</li>
        {% endfor %}
    </ul>
</body>
</html>
```
