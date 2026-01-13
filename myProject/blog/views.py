from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("<h1>Blog Home page</h1>")

def about(request):
    return HttpResponse("<h1>Blog About page</h1>")
