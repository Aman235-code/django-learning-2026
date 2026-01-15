## ORM (Object Relational Mapper) in Django

- converts python object fields(python class) into sql queries and vice versa

## Benefits
- no dependency on database
- less SQL - write only RAW queries
- Secure & Readable

## Django Models & Migrations 

- model -> represents Db table (class)
- in models.py file we are creating models (app folder)
- in blogs folder

```python
# models.py
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    email = models.EmailField(unique=True)
    enrollment_date = models.DateField(auto_now_add=True)
```

- after that we have run

```python
python manage.py makemigrations
```
- it creates a file inside the migrations folder
- then we have to migrate these changes in the db

```python
python manage.py migrate  
```

- if you made any changes in the models file then you have to run both the commands

## Retrieving Data from Database

- Django ORM QuerySet(Collection of rows)

- python manage.py shell -> shell command
- to retrieve data using shell

- all() -> fetches all records

```python
>>> from blog.models import Student
>>> student = Student.objects.all()
>>> print(student)
```

- to print the data 

```python
for s in student:
    print(s.name, s.age, s.city)
```
- get() -> fetches single record (error if multiple/none)
- to get one record

```python
>>> students = Student.objects.get(id = 1) 
>>> print(students)
```

- filter() -> fetchs record with condition

```python
>>> students = Student.objects.filter(age=20) 
>>> print(students)
```

