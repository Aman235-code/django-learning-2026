## Django ModelForms

- after creating models create forms.py inside the app folder

```python
from django import forms 
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'email']
```

- views.py

```python
from django.shortcuts import render
from .forms import StudentForm

# Create your views here.
def student_create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'student_success.html')
    return render(request, 'student_form.html', {'form': form})
```

- you can render the form like this

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student Add</title>
</head>
<body>
    <h2>Add Students Here</h2>
    <form method="POST">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">Submit</button>
    </form>
</body>
</html>
```

## ModelForms - List & Detail (Update & Delete)

- list & detail

```python
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})
```

- edit 

```python
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})
```

- delete

```python
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})
```

- html render for delete

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Students Delete</title>
</head>
<body>
    <h1>Confirm Delete Student</h1>
    <p>Are you sure you want to delete the student: <strong>{{ student.name }}</strong>?</p>
    <form method="POST">
        {% csrf_token %}
        <button type="submit">Yes, delete</button>
        <a href="{% url 'student_list' %}">Cancel</a>
    </form>
</body>
</html>
```

## Display Messages

```python
messages.debug() -> for developers
messages.info() -> General info for user
messages.success() -> positive action
messages.warning() -> Caution/Alert
messages.error() => Action failed / error
```

- in views you have to import messages 

```python
from django.contrib import messages

def show_message(request):
    messages.debug(request, 'This is a debug message.')
    messages.info(request, 'This is an informational message.')
    messages.success(request, 'This is a success message.')
    messages.warning(request, 'This is a warning message.')
    messages.error(request, 'This is an error message.')
    return render(request, 'show_message.html')
```

- in html

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Msg Data</title>
    <style>
        .debug {
            color: gray;
        }
        .info {
            color: blue;
        }
        .success {
            color: green;
        }
        .warning {
            color: orange;
        }
        .error {
            color: red;
        }
        ul {
            list-style-type: none;
            padding: 0;
        }
        li {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <h1>All Message Data</h1>
    {% if messages %}
    <ul>
        {% for message in messages %}
        <li class="{{message.tags}}">{{message}}</li>
        {% endfor %}
    </ul>
    {% else %}
    <p>No messages to display.</p>
    {% endif %}
</body>
</html>
```

- for debig message to show goto settings.py and add 
- from django.contrib.messages import constants as message_constants on line 14 and
- MESSAGE_LEVEL = message_constants.DEBUG at the last
- then you can see debug message