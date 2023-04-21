from .views import Home, AddTodo
from django.urls import path

urlpatterns = [
    path("", Home.as_view(), name="home"),
    path("", AddTodo.as_view(), name="add_todo"),
]
