from django.db.models import Case, Count, F, FloatField, Value, When
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
)

from .forms import TodoForm
from .models import Todo


# Create your views here.
class Home(ListView):
    model = Todo
    template_name = "index.html"
    context_object_name = "todos"
    ordering = ["done", "-date_created"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_count = self.object_list.count()
        done_count = self.object_list.filter(done=True).count()
        percentage_done = (done_count / total_count) * 100 if total_count > 0 else 0
        context["percentage_done"] = percentage_done
        return context


class AddTodo(CreateView):
    template_name = "index.html"
    model = Todo
    form_class = TodoForm
    success_url = reverse_lazy("home")


class DeleteTodo(DeleteView):
    model = Todo
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")


def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    todo.done = not todo.done
    todo.save()
    return redirect("home")
