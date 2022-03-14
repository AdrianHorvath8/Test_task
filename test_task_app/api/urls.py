from django.urls import path
from . import views

urlpatterns =[
    path("", views.get_routes,name="api_overview"),
    path("posts/", views.posts_view,name="posts"),
    path("post_create/", views.post_create,name="post_create"),
    path("post/<str:pk>/", views.post_view,name="post"),
    path("user/<str:pk>/", views.user_view,name="user"),
    path("post_update/<str:pk>/", views.post_update,name="post_update"),
    path("post_delete/<str:pk>/", views.post_delete,name="post_delete"),
]