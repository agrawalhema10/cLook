from django.db import models
# Create your models here.
class CriminalDetails(models.Model):
    name = models.CharField(max_length=50)
    cid = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='cLook/')
    status = models.CharField(max_length=10, default="Not Found", null=True)
    social_media_id= models.CharField(max_length=10, default="", null=True)
