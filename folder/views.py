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
    tasks = TaskSerializer(many=True, required=False)

    class Meta:
        model = Folder
        fields = ['id', 'name', 'tasks']

    def create(self, validated_data):
        Folder.objects.create(**validated_data)
        return Folder(**validated_data)


# Create your views here.
class FolderView(viewsets.ModelViewSet):
    queryset = Folder.objects.all()
    serializer_class = FolderSerializer
