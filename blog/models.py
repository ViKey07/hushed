
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    image = CloudinaryField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.title
