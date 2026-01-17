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

