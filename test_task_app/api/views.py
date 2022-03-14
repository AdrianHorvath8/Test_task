
from email import header
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from test_task_app.models import Post, User
from .serializers import PostSerializer, PostUpdateSerializer
import requests

@api_view(["GET"])
def get_routes(request):
    routes = [
        "GET /api",
        "GET /api/posts",
        "GET /api/post/:id",
        "GET /api/user/:id",
        "POST /api/post_create",
        "POST /api/post_update",
        "DELETE /api/post_delete",
    ]
    return Response(routes)

@api_view(["GET"])
def posts_view(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(["GET"])
def post_view(request, pk):
    try:
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(post, many=False)
    except:
        return Response( json.dumps([{"Error": "Post with that id does not exists"}]))
    return Response(serializer.data)

@api_view(["GET"])
def user_view(request, pk):
    try:
        user = User.objects.get(id=pk)
        posts= user.post_set.all()
        serializer = PostSerializer(posts, many=True)
    except:
        return Response( json.dumps([{"Error": "User with that id does not exists"}]))
    return Response(serializer.data)

@api_view(["POST"])
def post_create(request):
    serializer = PostSerializer(data=request.data)
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    posts = response.json()
    holder = False
    for i in posts:
        input_userId=request.data["user"]

        
        if input_userId == i["id"]:
            holder = True
            break 
        if holder == True:
            continue
        else:
            pass
    
        
    if holder == True:
        pass
    else:
        return Response( json.dumps([{"Error": "User with that id does not exists"}]))

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(["POST"])
def post_update(request, pk):
    try:
        post = Post.objects.get(id=pk)
        serializer = PostSerializer(instance=post, data=request.data)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
    except:
        return Response( json.dumps([{"Error": "Post with that id does not exists"}]))

    return Response(serializer.data)

@api_view(["DELETE"])
def post_delete(request, pk):
    try:
        post = Post.objects.get(id=pk)
        post.delete()
    except:
        return Response( json.dumps([{"Error": "Post with that id does not exists"}]))
    return Response("Post succsesfully delete!")