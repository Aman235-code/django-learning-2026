from django.shortcuts import render, get_object_or_404, redirect
from .forms import StudentForm
from .models import Student
from django.contrib import messages

# Create your views here.
def student_create(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'student_success.html')
    return render(request, 'student_form.html', {'form': form})

def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student_detail.html', {'student': student})

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

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        return redirect('student_list')
    return render(request, 'student_confirm_delete.html', {'student': student})

def show_message(request):
    messages.debug(request, 'This is a debug message.')
    messages.info(request, 'This is an informational message.')
    messages.success(request, 'This is a success message.')
    messages.warning(request, 'This is a warning message.')
    messages.error(request, 'This is an error message.')
    return render(request, 'show_message.html')
