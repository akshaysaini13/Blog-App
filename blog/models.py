from django.db import models

# Create your models here.

class BlogPost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=20)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):
        return self.title + " " + self.author