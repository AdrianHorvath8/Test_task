from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .forms import PostForm
from .models import Post, User
import requests

def home (request):
    q=request.GET.get("q") if request.GET.get("q") != None else ""
    posts=Post.objects.filter(
        Q(id__icontains=q)
    )
    context = {"posts":posts,}
    return render(request, "test_task_app/home.html", context)

def create_post(request):
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form":form}
    return render(request, "test_task_app/post_form.html", context)

def update_post(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)

    if request.method == "POST":
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect("home")

    context = {"form":form}
    return render(request, "test_task_app/post_form.html", context)

def delete_post(request,pk):
    post = Post.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    
    context = {"post":post}
    return render(request, "test_task_app/delete_post.html", context)



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
        try:
            userId=User.objects.filter(id=i["userId"])
            for id_user in userId:
                data = Post(
                    user = id_user,
                    title = i["title"],
                    body = i["body"],
                )
                data.save()
        except:
            HttpResponse("Please load users first !!")
        
    context = {}
    return render(request, "test_task_app/load_data.html", context)

def get_users(request):
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    posts = response.json()
    holder = False

    for i in posts:
        id = User.objects.all().values("id")

        for j in id:
            if j["id"] == i["id"]:
                holder = True
                break 
        if holder == True:
            continue
        else:
            pass

        data = User(
            name = i["name"],
            username = i["username"],
            mail = i["email"],
        )
        data.save()
    
    context = {}
    return render(request, "test_task_app/load_data.html", context)