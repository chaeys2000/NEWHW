from django.db import models
import datetime
from datetime import datetime, timedelta
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    cate = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)
    deadline = models.DateField(null=True)
    
    def __str__(self):
        return self.title

class Comment(models.Model):
   post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
   content = models.TextField()
   parent_comment = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE) 

   def __str__(self):
       return self.content