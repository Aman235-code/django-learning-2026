from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Blog Home page</h1>")

def about(request):
    return HttpResponse("<h1>Blog About page</h1>")

def post_details(request, post_id):
    return HttpResponse(f"<h1>Details of post {post_id}</h1>")

def user_profile(request, username):
    return HttpResponse(f"<h1>Profile of user {username}</h1>")

def article_by_year(request, year):
    return HttpResponse(f"<h1>Articles from the year {year}</h1>")

# def article_details(request, year, month):
#     return HttpResponse(f"<h1>Articles: from {year} - {month}</h1>")

def article_details(request, **kwargs):
    return HttpResponse(f"<h1>Articles from {kwargs}</h1>")