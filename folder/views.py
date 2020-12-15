from django.shortcuts import render
from rest_framework import viewsets
from .models import Folder
from task.models import Task
from rest_framework import serializers


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'date', 'name', 'notes', 'status']


class FolderSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True)
    class Meta:
        model = Folder
        fields = ['id', 'name', 'tasks']

# Create your views here.
class FolderView(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
