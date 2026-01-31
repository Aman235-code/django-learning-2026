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
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .models import Blog
# from .serializers import BlogSerializer
# from rest_framework import status 

# @api_view(['GET', 'POST'])
# def blog_list(request):
#     if request.method == 'GET':
#         blogs = Blog.objects.all()
#         serializer = BlogSerializer(blogs, many=True)
#         return Response(serializer.data)
    
#     elif request.method == 'POST':
#         serializer = BlogSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Token Authentication + IsAdminUser 
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication 
from rest_framework.authtoken.models import Token 

# api only for auth users
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def user_profile(request):
    user = request.user
    token, created = Token.objects.get_or_create(user=user)
    return Response({
        "username": user.username,
        "email": user.email,
        "is_staff": user.is_staff,
    })

# api only for admin users
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAdminUser])
def admin_panel(request):
    return Response({"message": f"Welcome to the admin panel, {request.user.username}"})