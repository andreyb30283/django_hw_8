# from .views import TaskCreateView, TaskListView, TaskStatsView, SubTaskDetailUpdateDeleteView, SubTaskListCreateView
# from django.urls import path
#
#
# urlpatterns = [
#     path('tasks/create/', TaskCreateView.as_view(), name='task-create'),
#     path('tasks/stats/', TaskStatsView.as_view(), name='task-stats'),
#     path('tasks/', TaskListView.as_view(), name='task-list'),
#
#
#     path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
#     path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
# ]
#
#
# ________________________________________________________________________________

# Web development: домашние задание 13 (Python)
# Домашнее задание: Замена функций представлений на Generic Views для
# задач и подзадач
# Цель:
# Изучить Generic Views.
# Используя Generic Views, замените существующие классы представлений
# для задач (Tasks) и подзадач (SubTasks) на соответствующие классы для
# полного CRUD (Create, Read, Update, Delete) функционала. Агрегирующий
# эндпойнт для статистики задач оставьте как есть. Реализуйте пагинацию,
# фильтрацию, поиск и сортировку для обоих наборов представлений.
# Задание 1: Замена представлений для задач (Tasks) на Generic Views
# Шаги для выполнения:
# Замените классы представлений для задач на Generic Views:
# Используйте ListCreateAPIView для создания и получения списка задач.
# Используйте RetrieveUpdateDestroyAPIView для получения, обновления и
# удаления задач.
# Реализуйте пагинацию, фильтрацию, поиск и сортировку:
# Добавьте пагинацию для списка задач.
# Реализуйте фильтрацию по полям status и deadline.
# Реализуйте поиск по полям title и description.
# Добавьте сортировку по полю created_at.
# Задание 2: Замена представлений для подзадач (SubTasks) на Generic Views
# Шаги для выполнения:
# Замените классы представлений для подзадач на Generic Views:
# Используйте ListCreateAPIView для создания и получения списка подзадач.
# Используйте RetrieveUpdateDestroyAPIView для получения, обновления и удаления подзадач.
# Реализуйте пагинацию, фильтрацию, поиск и сортировку:
# Добавьте пагинацию для списка подзадач.
# Реализуйте фильтрацию по полям status и deadline.
# Реализуйте поиск по полям title и description.
# Добавьте сортировку по полю created_at.
# Оформление ответа:
# Предоставьте решение: Прикрепите ссылку на гит.
# Скриншоты тестирования: Приложите скриншоты из браузера или Postman,
# подтверждающие успешное создание, обновление, получение и удаление
# данных через API.

from django.urls import path
from .views import TaskListCreateView, TaskRetrieveUpdateDestroyView, SubTaskListCreateView, \
    SubTaskRetrieveUpdateDestroyView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskRetrieveUpdateDestroyView.as_view(), name='subtask-detail'),
]
