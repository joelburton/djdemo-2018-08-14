from django.contrib import admin

from tasks.models import Task, TaskList


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "description", "done"]
    list_filter = ["done"]
    list_display_links = ["id", "title"]

class TaskInline(admin.StackedInline):
    model = Task

@admin.register(TaskList)
class TaskListAdmin(admin.ModelAdmin):
    inlines = [TaskInline]
