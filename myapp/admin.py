from django.contrib import admin

# Register your models here.
from .models import Task, Category, SubTask

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(SubTask)