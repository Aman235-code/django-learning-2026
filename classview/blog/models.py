from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # runs after every view
        return reverse('post_detail', args=[str(self.id)])
    
        