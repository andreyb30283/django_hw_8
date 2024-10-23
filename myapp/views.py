# from django.shortcuts import render
# from django.utils import timezone
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.renderers import JSONRenderer
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.db.models import Count, Q
# from rest_framework import generics, filters, status
# from django_filters.rest_framework import DjangoFilterBackend
# from .models import Task
# from .serializers import TaskSerializer, SubTaskCreateSerializer, TaskCreateSerializer
#
#
# class CustomPageNumberPagination(PageNumberPagination):
#     page_size = 4  # Количество объектов на странице
#     page_size_query_param = 'page_size'  # Позволяет пользователю передавать количество элементов на странице
#     max_page_size = 6  # Максимальное количество объектов на одной странице
#
# # '''
# class TaskCreateView(generics.CreateAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskCreateSerializer
#
#     def create(self, request, *args, **kwargs):
#         if isinstance(request.data, list):
#             serializer = self.get_serializer(data=request.data, many=True)
#         else:
#             serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         self.perform_create(serializer)
#         headers = self.get_success_headers(serializer.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
#
#     # def perform_create(self, serializer):
#     #     # Добавляем автора задачи перед сохранением  serializer.save(author=self.request.user)
#     #     serializer.save()
#
#
# class TaskStatsView(generics.RetrieveAPIView):
#     def get(self, request, *args, **kwargs):
#         total_tasks = Task.objects.count()
#         status_counts = Task.objects.values('status').annotate(count=Count('status'))
#         overdue_tasks = Task.objects.filter(deadline__lt=timezone.now(),
#                                             status__in=['New', 'In progress', 'Pending']).count()
#
#         return Response({
#             'total_tasks': total_tasks,
#             'status_counts': status_counts,
#             'overdue_tasks': overdue_tasks
#         })
#
#
# class TaskListView(generics.ListAPIView):
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
#     filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
#     filterset_fields = ['status', 'deadline']
#     ordering_fields = ['deadline']
#     pagination_class = CustomPageNumberPagination
# '''
# renderer_classes = [JSONRenderer]  # Отключает рендеринг HTML форм


#
# class TaskStatsView(APIView):
#     def get(self, request, *args, **kwargs):
#         total_tasks = Task.objects.count()
#         status_counts = Task.objects.values('status').annotate(count=Count('status'))
#         overdue_tasks = Task.objects.filter(deadline__lt=timezone.now(),
#                                             status__in=['New', 'In progress', 'Pending']).count()
#
#         return Response({
#             'total_tasks': total_tasks,
#             'status_counts': status_counts,
#             'overdue_tasks': overdue_tasks
#         })

'''
class CustomPageNumberPagination(PageNumberPagination):
    page_size = 4
    page_size_query_param = 'page_size'
    max_page_size = 6


class TaskCreateView(APIView):
    def post(self, request, *args, **kwargs):
        if isinstance(request.data, list):
            serializer = TaskSerializer(data=request.data, many=True)
        else:
            serializer = TaskSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class TaskStatsView(APIView):
    def get(self, request, *args, **kwargs):
        total_tasks = Task.objects.count()
        status_counts = Task.objects.values('status').annotate(count=Count('status'))
        overdue_tasks = Task.objects.filter(deadline__lt=timezone.now(),
                                            status__in=['New','In progress', 'Pending']).count()
        return Response({
            'total_tasks': total_tasks,
            'status_counts': status_counts,
            'overdue_tasks': overdue_tasks
        })


# Представление для списка задач с фильтрацией и пагинацией
class TaskListView(APIView):
    pagination_class = CustomPageNumberPagination

    def get(self, request, *args, **kwargs):
        queryset = Task.objects.all()

        # Фильтрация по статусу и дедлайну (если переданы параметры)
        status = request.query_params.get('status', None)
        deadline = request.query_params.get('deadline', None)

        if status:
            queryset = queryset.filter(status=status)
        if deadline:
            queryset = queryset.filter(deadline=deadline)

        # Пагинация
        paginator = self.pagination_class()
        page = paginator.paginate_queryset(queryset, request)

        if page is not None:
            serializer = TaskSerializer(page, many=True)
            return paginator.get_paginated_response(serializer.data)

        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)
'''

'''_________________________________________________________________________________________________'''
'''
# Список и создание подзадач

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import SubTask
from .serializers import SubTaskCreateSerializer, SubTaskSerializer
from rest_framework.generics import get_object_or_404


class SubTaskListCreateView(APIView):

    def get(self, request, *args, **kwargs):
        subtasks = SubTask.objects.all()
        serializer = SubTaskSerializer(subtasks, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = SubTaskCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Получение, обновление и удаление подзадач
class SubTaskDetailUpdateDeleteView(APIView):

    def get(self, request, pk, *args, **kwargs):
        subtask = get_object_or_404(SubTask, pk=pk)
        serializer = SubTaskSerializer(subtask)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        subtask = get_object_or_404(SubTask, pk=pk)
        serializer = SubTaskCreateSerializer(subtask, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, *args, **kwargs):
        subtask = get_object_or_404(SubTask, pk=pk)
        subtask.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)'''

'''__________________________________________________________________________'''

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from myapp.models import *
from .serializers import *
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend


class TaskListCreateView(ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["status", "deadline"]
    search_fields = ['title', "description"]
    ordering_fields = ['created_at']
    ordering = ['created_at']


class TaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SubTaskListCreateView(ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering = ['created_at']


class SubTaskRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskSerializer
