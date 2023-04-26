from django.urls import path

from .views import AddTodo, DeleteTodo, Home, UpdateTodo, test_view, toggle_todo

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("add", AddTodo.as_view(), name="add_todo"),
    path("delete/<str:id>", DeleteTodo.as_view(), name="delete_todo"),
    path("update/<str:id>", UpdateTodo.as_view(), name="update_todo"),
    path("test", test_view, name="test"),
    path("todos/<int:pk>/toggle/", toggle_todo, name="toggle_todo"),
]
