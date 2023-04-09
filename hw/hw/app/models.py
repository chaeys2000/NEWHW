from django.db import models
import datetime
from datetime import datetime, timedelta

# Create your models here.
class Post(models.Model):
    cate = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True, null=True)
    deadline = models.DateField(null=True)
    
    def __str__(self):
        return self.title
