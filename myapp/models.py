# Create your models here.
# Модель Task:
# Описание: Задача для выполнения.
# Поля:
# title: Название задачи. Уникально для даты.
# description: Описание задачи.
# categories: Категории задачи. Многие ко многим.
# status: Статус задачи. Выбор из: New, In progress, Pending, Blocked, Done
# deadline: Дата и время дедлайн.
# created_at: Дата и время создания. Автоматическое заполнение.
# Модель SubTask:
# Описание: Отдельная часть основной задачи (Task).
# Поля:
# title: Название подзадачи.
# description: Описание подзадачи.
# task: Основная задача. Один ко многим.
# status: Статус задачи. Выбор из: New, In progress, Pending, Blocked, Done
# deadline: Дата и время дедлайн.
# created_at: Дата и время создания. Автоматическое заполнение.
# Модель Category:
# Описание: Категория выполнения.
# Поля:
# name: Название категории.

from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Task(models.Model):
    title = models.CharField(max_length=255, unique=True, null=False)
    description = models.TextField(null=True)
    STATUS_CHOICES = [
        ('New', 'New'),
        ('In progress', 'In progress'),
        ('Pending', 'Pending'),
        ('Blocked', 'Blocked'),
        ('Done', 'Done')
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='New')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(Category)


class SubTask(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=Task.STATUS_CHOICES, default='New')
    deadline = models.DateTimeField()
    created_at = models.DateTimeField(auto_now_add=True)