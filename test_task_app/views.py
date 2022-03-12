from django.shortcuts import render
import requests
from .models import Post
def home (request):
    posts=Post.objects.all()
    context = {"posts":posts}
    return render(request,"test_task_app/home.html",context)


def get_data (request):
    response = requests.get("https://jsonplaceholder.typicode.com/posts")
    posts = response.json()
    holder = False
    for i in posts:
        id=Post.objects.all().values("id")

        for j in id:
            if j["id"] == i["id"]:
                holder = True
                break 
        if holder == True:
            continue
        else:
            pass

        data = Post(
            title = i["title"],
            body = i["body"],
        )
        data.save()
    
    context = {}
    return render(request,"test_task_app/load_data.html",context)