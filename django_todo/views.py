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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_count = self.object_list.count()
        done_count = self.object_list.filter(done=True).count()
        percentage_done = (done_count / total_count) * 100 if total_count > 0 else 0
        context["percentage_done"] = percentage_done
        return context


def test_view(request):
    # todo_queryset = Todo.objects.annotate(
    #     done_count=Count("id", filter=F("done")),
    #     total_count=Count("id"),
    #     percentage_done=F("done_count") / F("total_count") * 100,
    # ).order_by("done", "-date_created")

    todo_queryset = Todo.objects.all().order_by("done", "-date_created")

    total_count = todo_queryset.count()
    done_count = todo_queryset.aggregate(done_count=Count("id", filter=F("done"))).get(
        "done_count", 0
    )

    percentage_done = (done_count / total_count) * 100 if total_count > 0 else 0

    context = {
        "todos": todo_queryset,
        "percentage_done": percentage_done,
    }

    return render(request, "index.html", context)


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


# class ToggleTodoView(UpdateView):
#     model = Todo
#     fields = ['done']
#     success_url = reverse_lazy('todo_list')

#     def form_valid(self, form):
#         # Toggle the 'done' field value
#         self.object = form.save(commit=False)
#         self.object.done = not self.object.done
#         self.object.save()
#         return super().form_valid(form)

# def delete_todo(request, id):
#     data = get_object_or_404(Todo, id=id)
#     data.delete()
#     return redirect("home")
