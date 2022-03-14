from rest_framework.serializers import ModelSerializer
from test_task_app.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields= "__all__"

class PostUpdateSerializer(ModelSerializer):
    class Meta:
        model=Post
        fields= "__all__"
        exclude = ["user"]