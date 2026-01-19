## Authentication & Permissions

### Superuser permissions

- first make migrations and migrate to see the database
- create superuser using this command
- python manage.py createsuperuser
- goto this link http://127.0.0.1:8000/admin
- enter the credentials

- superuser has all the permissions
- when you create a new user he only has Active permission
- when you login using this new user credentials you cannot login, because staff permissions not checked
- so to give this staff status permission to this new user you have to login using admin account
and check on staff status
- then you can login using this newuser credentials
- but this user has no permission to view/edit the data

- to give him the permissions login using admin account and in user permissions you can select and choose the permissions for that user
- we can give him the permissions say can add/change/view/delete the user
- when you login using this newuser account after giving him the permissions that user has permission to view/change/delete/update the user.

### Group Permissions

- login using admin account
- click on groups -> add group
- here you can make a group having some permssions for that group
- then you can assign that group to any user so that user has the permissions as that of the group
- no need to assign the permissions for that user individually 

### User Authentication

- we can use django's builtin forms 

```python
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ResgistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exists")
        return email
```

- we can import in in view as 

```python
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .forms import ResgistrationForm

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

# without login this decorator redirects u to the login page
@login_required(login_url='login')
def dashboard(request):
    return render(request, 'accounts/dashboard.html')   
```