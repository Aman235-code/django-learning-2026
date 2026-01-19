from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import ResgistrationForm, ProfileForm
from .models import Profile

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ResgistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # auto login after registration
            messages.success(request, 'Registration successful and logged in.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Registration failed. Please correct the errors below.')
    else:
        form = ResgistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'accounts/login.html')


def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been logged out.')
    return redirect('login')

@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')   

def upload_profile(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile Picture Uploaded successfully')
            return redirect('view_profile')
        else:
            messages.error(request, "Error Uploading profile picture")
    else:
        form = ProfileForm()
    return render(request, 'accounts/upload_profile.html', {'form':form})

def view_profile(request):
    profile = Profile.objects.all()
    return render(request, 'accounts/view_profile.html', {'profiles':profile})