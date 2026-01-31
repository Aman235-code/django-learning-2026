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






    

