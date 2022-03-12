from django.db import models

class Post(models.Model):
    #user
    title = models.CharField(max_length=200,)
    body = models.TextField(null=True,blank=True)