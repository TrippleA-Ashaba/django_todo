from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, TemplateView

from .forms import TodoForm
from .models import Todo


# Create your views here.
class Home(ListView):
    template_name = "index.html"
    context_object_name = "todos"
    model = Todo
    ordering = ["done", "-date_created"]


class AddTodo(CreateView):
    template_name = "index.html"
    model = Todo
    form_class = TodoForm
    success_url = "/"
