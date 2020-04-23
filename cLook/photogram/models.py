from django.db import models

# Create your models here.
class Register(models.Model):
    username= models.CharField(max_length=50,null=True,default="")
    password=models.CharField(max_length=50,null=True,default="")
    email=models.CharField(max_length=50,null=True,default="")
    location=models.CharField(max_length=50,null=True,default="")
    profile_pic= models.ImageField(upload_to='photogram/')
