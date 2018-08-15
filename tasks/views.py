from django.shortcuts import render
from django.views import generic

from tasks.models import Task, TaskList


class TaskListView(generic.ListView):
    def get_queryset(self):
        if True:
            return Task.objects.all()

class TaskDetailView(generic.DetailView):
    model = Task

class TaskListDetailView(generic.DetailView):
    model = TaskList

class TaskListListView(generic.ListView):
    model = TaskList
