from .views import TaskCreateView, TaskListView, TaskStatsView, SubTaskDetailUpdateDeleteView, SubTaskListCreateView
from django.urls import path


urlpatterns = [
    path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
    path('tasks/', TaskListView.as_view(), name='task-list'),


    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
]
