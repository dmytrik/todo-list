from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic, View
from django.urls import reverse_lazy, reverse
from django.db import transaction

from task.models import Task, Tag
from task.forms import TaskForm


class TodoListView(View):

    @staticmethod
    def get(request):
        if request.user.is_authenticated:
            todos = request.user.tasks.order_by("is_done").order_by("-deadline")
            context = {
                "task_list": todos
            }
            return render(request, "task/task_list.html", context=context)

        return HttpResponseRedirect(reverse("accounts:login"))


class TodoCreateView(View):

    @staticmethod
    def get(request):
        context = {
            "form": TaskForm
        }
        return render(request, "task/create_todo.html", context=context)

    @staticmethod
    def post(request):
        form = TaskForm(request.POST)
        if form.is_valid():
            with transaction.atomic():
                task = Task.objects.create(content=form.cleaned_data["content"], deadline=form.cleaned_data["deadline"])
                task.tags.set(form.cleaned_data["tags"])
                request.user.tasks.add(task)
            return HttpResponseRedirect(reverse("task:task-list"))
        context = {
            "form": TaskForm,
            "error": "Invalid data"
        }
        return render(request, "task/create_todo.html", context=context)

class TodoUpdateView(generic.UpdateView):
    model = Task
    fields = ("content", "deadline", "tags")
    queryset = Task.objects.prefetch_related("tags")


class TodoDeleteView(generic.DeleteView):
    model = Task
    success_url = reverse_lazy("task:task-list")


class TodoCompleteView(View):

    @staticmethod
    def get(request, pk: int):
        with transaction.atomic():
            todo = Task.objects.get(id=pk)
            todo.is_done = True
            todo.save()
        return HttpResponseRedirect(reverse("task:task-list"))


class TodoUndoView(View):

    @staticmethod
    def get(request, pk: int):
        with transaction.atomic():
            todo = Task.objects.get(id=pk)
            todo.is_done = False
            todo.save()
        return HttpResponseRedirect(reverse("task:task-list"))


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = ("name",)


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = ("name",)


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("task:tag-list")
