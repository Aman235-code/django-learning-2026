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
