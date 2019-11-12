from django.db import models


class Post(models.Model):
    name = models.CharField(max_length=100)
    age = models.CharField(max_length=100)
    date = models.DateField(auto_now=True,null=True,blank=True)
    img=models.ImageField(upload_to='add')
