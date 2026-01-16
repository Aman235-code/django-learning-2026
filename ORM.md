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
python manage.py makemigrations appname (only changes apply to appname)
```
- it creates a file inside the migrations folder
- then we have to migrate these changes in the db

```python
python manage.py migrate  
```

- if you made any changes in the models file then you have to run both the commands

## Retrieving Data from Database

### Using Shell

- Django ORM QuerySet(Collection of rows)

- python manage.py shell -> shell command
- to retrieve data using shell

- to create the row

```python
from portfolio.models import Student
Student.objects.create(name="Aman", age=20, city="Delhi")
```

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

- ordering and chaining

```python
>>> from blog.models import Student
>>> students = Student.objects.all().order_by("name")
>>> students = Student.objects.all().order_by("age")
>>> students = Student.objects.all().order_by("-age") # descending
>>> print(students)
```

- chaining 

```python
>>> students = Student.objects.filter(city="Delhi").filter(age__gte = 18).order_by("name") 
>>> print(students)  
```

- exclude (skip this row)

```python
>>> students = Student.objects.exclude(city="Delhi")   
```

- values (returns data in the frm of dictionaries)

```python
students = Student.objects.values("name", "city") 
```

- value list -> in form of List

```python
>>> students = Student.objects.values_list("name", flat=True)
```

- First & Last

```python
>>> students = Student.objects.first()       
>>> students = Student.objects.last()
```       

- count - returns no of rows

```python
>>> students = Student.objects.count()
```

### Using Template

- once you have defined models created data and migrated in views.py you can get the data through

```python
from .models import Student

def student_list(request):
    students = Student.objects.all() # retrives all the rows from the table Student
    return render(request, 'portfolio/student_list.html', {'students': students})
```

