from django.shortcuts import render, redirect
from .models import Student, Contact
from django.http import HttpResponse

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, 'portfolio/student_list.html', {'students': students})

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