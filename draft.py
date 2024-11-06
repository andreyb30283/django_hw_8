from datetime import date, timedelta
from django.db import models
from myapp.models import SubTask, Task
from django.utils import timezone
# Создаем основную задачу
task = Task.objects.create(
    title="Prepare presentation",
    description="Prepare materials and slides for the presentation",
    status="New",
    deadline=timezone.now() + timedelta(days=3))


# Создаем подзадачи
SubTask.objects.create(task=task, title="Gather information",
                       description="Find necessary information for the presentation",
                       status="New", deadline=date.today() + timedelta(days=2))
SubTask.objects.create(task=task, title="Create slides",
                       description="Create presentation slides",
                       status="New", deadline=date.today() + timedelta(days=1))

SubTask.objects.bulk_create([SubTask(task=task[0], title="Gather information",
                       description="Find necessary information for the presentation",
                       status="New", deadline=timezone.now() + timedelta(days=2)),
                        SubTask(task=task[0], title="Create slides",
                       description="Create presentation slides",
                       status="New", deadline=timezone.now() + timedelta(days=1))])





# Задачи со статусом "New"
new_tasks = Task.objects.filter(status='New')

# Подзадачи с просроченным статусом "Done"
overdue_done_subtasks = SubTask.objects.filter(status='Done', deadline__lt=timezone.now())

task = Task.objects.get(title="Prepare presentation")
task.status = 'In progress'
task.save()

# Изменяем срок выполнения для "Gather information" на два дня назад
subtask = SubTask.objects.get(title="Gather information")
subtask.deadline = timezone.now() - timedelta(days=2)
subtask.save()

# Изменяем описание для "Create slides"
subtask = SubTask.objects.get(title="Create slides")
subtask.description = "Create and format presentation slides"
subtask.save()

# Удаляем задачу и все связанные подзадачи
task = Task.objects.get(title="Prepare presentation")
task.delete()  # Это автоматически удалит все связанные SubTasks благодаря on_delete=models.CASCADE

# _______________________________________________________________
# Выполните запросы:
# Создание записей:
# Task:
# title: "Prepare presentation".
# description: "Prepare materials and slides for the presentation".
# status: "New".
# deadline: Today's date + 3 days.
# SubTasks для "Prepare presentation":
# title: "Gather information".
# description: "Find necessary information for the presentation".
# status: "New".
# deadline: Today's date + 2 days.
# title: "Create slides".
# description: "Create presentation slides".
# status: "New".
# deadline: Today's date + 1 day.
# Чтение записей:
# Tasks со статусом "New":
# Вывести все задачи, у которых статус "New".
# SubTasks с просроченным статусом "Done":
# Вывести все подзадачи, у которых статус "Done", но срок выполнения истек.
# Изменение записей:
# Измените статус "Prepare presentation" на "In progress".
# Измените срок выполнения для "Gather information" на два дня назад.
# Измените описание для "Create slides" на "Create and format presentation slides".
# Удаление записей:
# Удалите задачу "Prepare presentation" и все ее подзадачи.
# Оформите ответ:
#
# Прикрепите все выполненные запросы (код) и скриншоты с консоли к ответу на домашнее задание.