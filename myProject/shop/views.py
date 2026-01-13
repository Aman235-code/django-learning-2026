from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("<h1>Shop Home page</h1>")

def products(request):
    return HttpResponse("<h1>Shop Products page</h1>")

def product_list(request):
    return render(request, 'shop/product_list.html')
