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



