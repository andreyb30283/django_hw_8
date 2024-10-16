from rest_framework import serializers

from .models import *


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'deadline']


class SubTaskCreateSerializer(serializers.ModelSerializer):
    create_at = serializers.DateTimeField(read_only=True)  # Поле доступно только для чтения

    class Meta:
        model = SubTask
        fields = '__all__'


class CategoryCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data.get('name')
        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError('error validation')
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        name = validated_data.get('name', instance.name)
        if Category.objects.filter(name=name).exclude(pk=instance.pk).exists():
            raise serializers.ValidationError("Категория с таким названием уже существует.")
        instance.name = name
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class SubTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        # fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at']
        fields = '__all__'

class TaskDetailSerializer(serializers.ModelSerializer):
    subtasks = SubTaskSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at', 'subtasks']


from django.utils import timezone

class TaskCreateSerializer(serializers.ModelSerializer):

    def validate_deadline(self, value):
        print(value)
        if value < timezone.now():
            raise serializers.ValidationError("Дата дедлайна не может быть в прошлом.")
        return value

    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'status', 'deadline', 'created_at']


