from django.urls import path

from .views import AddTodo, DeleteTodo, Home, toggle_todo

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("add", AddTodo.as_view(), name="add_todo"),
    path("delete/<str:id>", DeleteTodo.as_view(), name="delete_todo"),
    path("todos/<int:pk>/toggle/", toggle_todo, name="toggle_todo"),
]
