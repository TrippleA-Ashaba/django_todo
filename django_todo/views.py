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
    try:
        done_todos = Todo.objects.filter(done=True).count()
        all_todos = Todo.objects.all().count()
        completed = (done_todos / all_todos) * 100
    except ZeroDivisionError:
        completed = 0

    extra_context = {"completed": completed}


# def home_view(request):
#     todos = Todo.objects.all().order_by("done", "-date_created")
#     done_todos = todos.filter("done")
#     val = done_todos.count()
#     completed_percentage = (val / todos.count()) * 100
#     return render(
#         request, "home.html", {"todos": todos, "completed": completed_percentage}
#     )


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
