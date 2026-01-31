## Django Rest Framework

- setup
- after creating project & app run this command

```python
pip install django djangorestframework
```

- in settins.py add 

```bash
 'rest_framework',
```

- create serializers.py inside the app folder

```python
from rest_framework import serializers  # type: ignore
from .models import Student 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        # fields = ['id', 'name', 'age', 'city']
        fields = '__all__' # all fields
```

- in views file

```python
from django.shortcuts import render
from rest_framework.decorators import api_view # type: ignore
from .models import Student 
from .serializers import StudentSerializer
from rest_framework.response import Response # type: ignore

# Create your views here.
@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)
```

## Read API - Django Rest Framework

- same as above

```python
class Student2Serializer(serializers.ModelSerializer):
     class Meta:
        model = Student2
        fields = '__all__' # all fields
```


```python
@api_view(['GET'])
def get_students(request):
    students = Student2.objects.all()
    serializer = Student2Serializer(students, many=True)
    return Response(serializer.data)
```

## POST API - DRF

```python
@api_view(['POST'])
def add_student(request):
    serializer = Student2Serializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
```

## PUT API - DRF  - send all the fields

```python
@api_view(['PUT'])
def update_student(request, pk):
    try:
        student = Student2.objects.get(id=pk)
    except Student2.DoesNotExist:
        return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
    
    serializer = Student2Serializer(student, data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
```

## PATCH API - DRF - only one field to update

```python
@api_view(['PUT', 'PATCH'])
def update_student(request, pk):
    try:
        student = Student2.objects.get(id=pk)
    except Student2.DoesNotExist:
        return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
    # Partial update 
    if request.method == 'PATCH':
        serializer = Student2Serializer(student, data = request.data, partial=True)
    else:
        serializer = Student2Serializer(student, data = request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
```

## Delete API - DRF

```python

@api_view(['DELETE'])
def delete_student(request, pk):
    try:
        student = Student2.objects.get(id=pk)
    except Student2.DoesNotExist:
        return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
    
    student.delete()
    return Response({"message":"Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
```

## DRF CRUD Using API VIEW

```python
from rest_framework.views import APIView # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status  # type: ignore
from .models import Student 
from .serializers import StudentSerializer

# CRUD operation using APIView
class StudentAPI(APIView):
    # Read all or single data
    def get(self, request, pk=None):
        if pk:
            try:
                student = Student.objects.get(id=pk)
                serializer = StudentSerializer(student)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
        else:
            # read all data
            student = Student.objects.all()
            serializer = StudentSerializer(student, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
    # Create Data (POST)
    def post(self, request, pk=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    # Update Data (PUT)
    def put(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
        except Student.DoesNotExist:
            return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)
    
    # Delete Data (DELETE)
    def delete(self, request, pk):
        try:
            student = Student.objects.get(id=pk)
            student.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Student.DoesNotExist:
            return Response({"error":"Student not found"},status=status.HTTP_404_NOT_FOUND)
```

- urls file

```python
from django.urls import path
from .views import StudentAPI

urlpatterns = [
    path('students/', StudentAPI.as_view()),
    path('students/<int:pk>',StudentAPI.as_view())
]
```

## DRF CRUD Using Generic API View + Mixins

```python
from rest_framework import generics, mixins
from .models import Student 
from .serializers import StudentSerializer

class StudentListCreateAPI(
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin
):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # Read all data
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class StudentRetrieveUpdateDeleteAPI(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    # single data
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    # update
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
```

- urls file

```python
from django.urls import path
from .views import StudentListCreateAPI, StudentRetrieveUpdateDeleteAPI

urlpatterns = [
    path('students/', StudentListCreateAPI.as_view()),
    path('students/<int:pk>',StudentRetrieveUpdateDeleteAPI.as_view())
]
```

## DRF CRUD Using ModelViewSet + Routers

```python
from rest_framework import viewsets
from .models import Student 
from .serializers import StudentSerializer

# Full CRUD 
class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
```

- urls file

```python
from django.urls import path, include 
from rest_framework.routers import DefaultRouter # type: ignore
from .views import StudentViewSet

router = DefaultRouter()
router.register('students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls))
]
```


## DRF Authentication & Permissions

### Authentication

- Basic Authentication 
- Session Authentication
- Token Authentication
- JWT Authentication

### Permissions
- AllowAny
- IsAuthenticated
- IsAdminUser
- IsAuthenticatedOrReadOnly

### Basic Authentication + AllowAny & IsAuthenticated

- settings.py at bottom

```python
# REST Frsmework COnfiguration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

- urls file 

```python
from django.urls import path 
from . import views 

urlpatterns = [
    path('public/', views.public_view, name='public_view'),
    path('private/', views.private_view, name='private_view'),
]
```

- views

```python
from rest_framework.decorators import api_view, permission_classes # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework.permissions import IsAuthenticated, AllowAny # type: ignore

# public view access without authentication
@api_view(['GET'])
@permission_classes([AllowAny])
def public_view(request):
    return Response({"message": "This is a public view"})

# private view accessible only to authenticated users
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def private_view(request):
    return Response({"message": f"Hello, {request.user.username}. This is a private view."})
```

### Session Authentication + IsAuthenticatedOrReadOnly

- settings file

```python
# REST Frsmework COnfiguration

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
         'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
```

- create models and serializers for this

- urls file

```python
from django.urls import path 
from . import views 

urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),
]
```

- views

```python
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status 

@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```

### Token Authentication + IsAdminUser 

- for this one in settings.py installed apps add this 

```python
 'rest_framework',
 'rest_framework.authtoken',
 'api',
]
```

- run migarations (migrate comand)
- below settings.py 

```python
# REST Frsmework COnfiguration

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 'rest_framework.authentication.BasicAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        # 'rest_framework.permissions.IsAuthenticated',
        #  'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```

- create signals.py in app folder

```python
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver 
from django.core.mail import send_mail
from rest_framework.authtoken.models import Token # type: ignore

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
```

- then in apps.py 

```python
from django.apps import AppConfig


class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        import api.signals
```

- urls file 

```python
from django.urls import path 
from . import views 
from rest_framework.authtoken.views import obtain_auth_token # type: ignore

urlpatterns = [
    path('auth-token/', obtain_auth_token, name='api_token_auth'),
    path('profile/', views.user_profile, name='user_profile'),
    path('admin-panel/', views.admin_panel, name='admin_panel'),
]
```

- views file

```python
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication 
from rest_framework.authtoken.models import Token 

# api only for auth users
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    return Response({
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff,
    })

# api only for admin users
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def admin_panel(request):
    return Response({"message": f"Welcome to the admin panel, {request.user.username}"})
```

- in postman

```python
http://127.0.0.1:8000/api/auth-token/ (POST)

{
  "username":"admin",
  "password": "admin"
}
```

- you'll get a token
- if you hit this http://127.0.0.1:8000/api/profile/ without any token it gives unauthrozied
- goto header Authorization Token (your token) then you'll get the result
- same for this url (GET) http://127.0.0.1:8000/api/admin-panel/ pass Token (token) in headers
- if you create a new user in admin panel the default is_staff = false so if you hit admin panel it says You do not have permission to perform this action

### JWT Authentication + IsAuthenticatedOrReadOnly

- for this you need to run 

```python
pip install djangorestframework-simplejwt
```

- in settings installed apps

```python
   'api',
    'rest_framework',
    'rest_framework_simplejwt',
]
```

- settings.py at the last

```python
# Rest Frameork Configuaration
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
    ],
}
```

- urls of Main project

```python
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView # type: ignore


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]
```

- views

```python
from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view, permission_classes # type: ignore
from rest_framework.permissions import IsAuthenticatedOrReadOnly # type: ignore

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == 'GET':
        return Response({"message": "List of posts public"})
    elif request.method == 'POST':
        return Response({"message": f"{request.user.username} only auth users post data"})
```

- GET
- http://127.0.0.1:8000/api/posts/
- you'll see -> 

```python
{
  "message": "List of posts public"
}
```

- post 
- generate token
- http://127.0.0.1:8000/api/token/ 
- body

```python
{
  "username": "admin",
  "password": "admin"
}
```

- you'll get both refresh and access token

- then go to http://127.0.0.1:8000/api/posts/ (post)
- goto body and paste

```python
{
  "message":"test"
}
```

- and paste that accesstoken in headers Authorization Bearer (token)
- then you'll see this

```python
{
  "message": "admin only auth users post data"
}
```

- for refresh token 
- http://127.0.0.1:8000/api/token/refresh (POST)
- in body 

```python
{
    "refresh": (refresh token got from api/token)
}
```
