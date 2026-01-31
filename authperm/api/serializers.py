from rest_framework import serializers  # type: ignore
from .models import Blog 

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__' # all fields