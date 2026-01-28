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