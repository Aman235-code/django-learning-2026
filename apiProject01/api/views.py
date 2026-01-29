from django.shortcuts import render
from rest_framework.decorators import api_view # type: ignore
from .models import Student, Student2
from .serializers import StudentSerializer, Student2Serializer
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore

# Create your views here.
@api_view(['GET'])
def student_list(request):
    students = Student.objects.all()
    serializer = StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_students(request):
    students = Student2.objects.all()
    serializer = Student2Serializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def add_student(request):
    serializer = Student2Serializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

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
    


