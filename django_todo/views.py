from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from .models import Todo


# Create your views here.
class Home(ListView):
    template_name = "index.html"
    context_object_name = "todos"
    model = Todo


class AddTodo(CreateView):
    template_name = "index.html"
    model = Todo
