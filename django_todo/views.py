from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    TemplateView,
    DeleteView,
    UpdateView,
)

from .forms import TodoForm
from .models import Todo
from django.db.models import Count, F, FloatField, Case, When, Value


# Create your views here.
class Home(ListView):
    model = Todo
    template_name = "index.html"
    context_object_name = "todos"
    ordering = ["done", "-date_created"]

    # get completed percentage
    try:
        done_todos = Todo.objects.filter(done=True).count()
        all_todos = Todo.objects.all().count()
        completed = (done_todos / all_todos) * 100
    except ZeroDivisionError:
        completed = 0

    extra_context = {"completed": completed}


def test_view(request):
    todo_queryset = Todo.objects.all()
    done = todo_queryset.filter(done=True).count()
    percentage_done = (
        ((done / todo_queryset.count()) * 100) if len(todo_queryset) > 0 else 0
    )

    return render(
        request,
        "index.html",
        {"todos": todo_queryset, "done": done, "percent": percentage_done},
    )


class AddTodo(CreateView):
    template_name = "index.html"
    model = Todo
    form_class = TodoForm
    success_url = "/test"


class DeleteTodo(DeleteView):
    model = Todo
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")


class UpdateTodo(UpdateView):
    model = Todo
    pk_url_kwarg = "id"
    fields = ["done"]
    success_url = reverse_lazy("home")


def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.done = not todo.done
    todo.save()
    return redirect("test")


# def delete_todo(request, id):
#     data = get_object_or_404(Todo, id=id)
#     data.delete()
#     return redirect("home")
