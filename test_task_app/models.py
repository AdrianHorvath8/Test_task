from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200,)
    username = models.CharField(max_length=200,)
    mail = models.CharField(max_length=200,)

    def __str__(self):
        return self.username

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200,)
    body = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.title