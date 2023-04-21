from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, DeleteView

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


class DeleteTodo(DeleteView):
    model = Todo
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")


def delete_todo(request, id):
    data = get_object_or_404(Todo, id=id)
    data.delete()
    return redirect("home")
