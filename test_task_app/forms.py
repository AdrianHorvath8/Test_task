from dataclasses import field
from operator import mod
from statistics import mode
import django
from django.forms import ModelForm
from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = "__all__"