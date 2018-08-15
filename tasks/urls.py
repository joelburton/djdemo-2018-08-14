from django.urls import path

from tasks import views

urlpatterns = [
    path('', views.TaskListView.as_view()),
    path('<int:pk>/', views.TaskDetailView.as_view(), name="task_detail"),
    path('lists/', views.TaskListListView.as_view()),
    path('lists/<int:pk>/', views.TaskListDetailView.as_view())

]