from django.db import models

# Create your models here.

class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=20)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)


# class myUsers(models.Model):
#     username = models.CharField(max_length=50)
#     firstname = models.CharField(max_length=50)
#     lastname = models.CharField(max_length=50)
#     email = models.CharField(max_length=50)
#     password1 = models.CharField(max_length=20)
    
#     def __str__(self):
#         return self.fname + " " + self.lname 