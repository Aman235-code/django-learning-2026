from django.shortcuts import render
from .models import Post, MainBlog
from django.core.paginator import Paginator
from django.db.models import Q

# Create your views here.
def post_list(request):
    post = Post.objects.all().order_by('id')
    paginator = Paginator(post, 4) # show 4 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'blog/post_list.html', {'page_obj': page_obj})

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

    