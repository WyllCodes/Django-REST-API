from django.db import models 
from datetime import deltatime 

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    ceated = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title