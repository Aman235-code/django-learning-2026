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