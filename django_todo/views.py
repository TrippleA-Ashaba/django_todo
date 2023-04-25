from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, TemplateView, DeleteView

from .forms import TodoForm
from .models import Todo
from django.db.models import Count, F, FloatField, Case, When


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
    todo_queryset = Todo.objects.values("id", "title", "done").annotate(
        percentage_done=Count(Case(When(done=True, then=1), output_field=FloatField()))
        * 100.0
        / Count("id")
    )
    return render(request, "index.html", {"todos": todo_queryset})


class AddTodo(CreateView):
    template_name = "index.html"
    model = Todo
    form_class = TodoForm
    success_url = "/test"


class DeleteTodo(DeleteView):
    model = Todo
    pk_url_kwarg = "id"
    success_url = reverse_lazy("home")


def delete_todo(request, id):
    data = get_object_or_404(Todo, id=id)
    data.delete()
    return redirect("home")
