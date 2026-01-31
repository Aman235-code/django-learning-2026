# Basic Authentication + AllowAny & IsAuthenticated

# from rest_framework.decorators import api_view, permission_classes # type: ignore
# from rest_framework.response import Response # type: ignore
# from rest_framework.permissions import IsAuthenticated, AllowAny # type: ignore

# # public view access without authentication
# @api_view(['GET'])
# @permission_classes([AllowAny])
# def public_view(request):
#     return Response({"message": "This is a public view"})

# # private view accessible only to authenticated users
# @api_view(['GET'])
# @permission_classes([IsAuthenticated])
# def private_view(request):
#     return Response({"message": f"Hello, {request.user.username}. This is a private view."})


# Session Authentication + IsAuthenticatedOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer
from rest_framework import status 

@api_view(['GET', 'POST'])
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)