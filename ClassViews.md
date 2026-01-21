## Class-Based Vies (CBVs)

### Function Based Views (FBV)

- Normal python functions that handles the requests
- for each http method we have to manually write this condition 
- if request.method == "POST" etc
- flexible, simple for beginners
- example

```python
from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})
```

### Class Based Views (CBV)

- Python classes that inherits from django's built-in view class
- code reusability, less boilerplate code
- HTTP methods(get, post) we can defined them directly inside the class
- example

```python
from django.views import View
from django.shortcuts import render
from .models import Post

class PostListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/post_list.html', {'posts': posts})
```

- here for every view if you want to go to that template you can make changes in the models file 

```python
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # runs after every view
        return reverse('post_detail', args=[str(self.id)])
```

- urls file

```python
from django.urls import path
# from . import views 
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post_detail"),
    path('post/new/', PostCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(), name='post_delete')
]
```

- views file

```python
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post

# List View
class PostListView(ListView):
    model = Post 
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

# Detail View
class PostDetailView(DetailView):
    model = Post 
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

# Create View
class PostCreateView(CreateView):
    model = Post 
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

# Update View
class PostUpdateView(UpdateView):
    model = Post 
    template_name = 'blog/post_form.html'
    fields = ['title', 'content']

# Delete View
class PostDeleteView(DeleteView):
    model = Post 
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list') # it'll not move to post detail page
```