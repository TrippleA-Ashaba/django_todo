from .views import Home, AddTodo, delete_todo, DeleteTodo
from django.urls import path

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("add", AddTodo.as_view(), name="add_todo"),
    path("delete/<str:id>", DeleteTodo.as_view(), name="delete_todo"),
]
