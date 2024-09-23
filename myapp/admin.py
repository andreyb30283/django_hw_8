from django.contrib import admin

# Register your models here.
from .models import Task, Category, SubTask

class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'creates_at')

class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'deadline', 'created_at', 'task')

admin.site.register(Task, TaskAdmin)
admin.site.register(Category)
admin.site.register(SubTask, SubTaskAdmin)