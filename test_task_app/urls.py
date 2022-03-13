from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("get_data/",views.get_data,name="get_data"),
    path("get_users/",views.get_users,name="get_users"),
    path("create_post/",views.create_post,name="create_post"),
    path("update_post/<str:pk>/",views.update_post,name="update_post"),
    path("delete_post/<str:pk>/",views.delete_post,name="delete_post"),
]
