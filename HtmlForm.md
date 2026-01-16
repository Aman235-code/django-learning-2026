## HTML Forms in Django

```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('contact/', views.contact, name='contact'),
    path('submit/', views.submit_form, name='submit_form'),
]
```

```python
def contact(request):
    return render(request, 'contact.html')

def submit_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        if name and message:
            Contact.objects.create(name=name, message=message)
            return HttpResponse(f"Thank you, {name}, for your message!")
        else:
            return HttpResponse("Name and message cannot be empty.", status=400)
    
    return redirect('contact')
```

```python
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login page </title>
</head>
<body>
    <form action="{% url 'submit_form' %}" method="POST">
        {% csrf_token %}
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="message">Message:</label><br>
        <textarea id="message" name="message" rows="4" cols="50" required></textarea><br><br>
        
        <input type="submit" value="Submit">
    </form>
</body>
</html>
```