from django.db import models
from django.urls import reverse


class Task(models.Model):
    """A task for the site."""

    title = models.CharField(
        max_length=50,
        unique=True,
    )

    description = models.TextField(
        blank=True,
    )

    done = models.BooleanField(default=False)

    tasklist = models.ForeignKey(
        "TaskList",
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("task_detail", kwargs={"pk": self.id})


class TaskList(models.Model):
    """list of tasks."""

    title = models.CharField(
        max_length=50,
        unique=True
    )

    def __str__(self):
        return self.title

    def num_undone(self):
        """How many tasks are incomplete on this list?"""

        undone = [t for t in self.task_set.all() if not t.done]
        return len(undone)

















