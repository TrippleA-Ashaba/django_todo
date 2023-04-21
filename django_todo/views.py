from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, DeleteView

from .forms import TodoForm
from .models import Todo


# Create your views here.
class Home(ListView):
    model = Todo
    template_name = "index.html"
    context_object_name = "todos"
    ordering = ["done", "-date_created"]

    # get completed percentage
    done_todos = Todo.objects.filter(done=True).count()
    undone_todos = Todo.objects.filter(done=False).count()
    completed = (done_todos / undone_todos) * 100

    extra_context = {"completed": completed}


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
