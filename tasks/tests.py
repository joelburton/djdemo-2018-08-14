from django.test import TestCase, Client

from tasks.models import Task, TaskList


class TaskTestCase(TestCase):
    def test_create(self):
        task = Task.objects.create(title="Clean car", done=True)
        self.assertEqual(task.done, True)

    def test_can_be_in_list(self):
        tasklist = TaskList.objects.create(title="Work Stuff")
        self.assertEqual(tasklist.title, "Work Stuff")
        task = Task.objects.create(title="Clean car", done=True, tasklist=tasklist)
        self.assertEqual(task.tasklist, tasklist)


class TaskListTestCase(TestCase):
    def test_create(self):
        tasklist = TaskList.objects.create(title="Work Stuff")
        self.assertEqual(tasklist.title, "Work Stuff")

    def test_list_view(self):
        c = Client()
        resp = c.get("/tasks/lists/1/")
        self.assertContains(resp.content, "Wash Cat")