from django.db import models
from datetime import datetime
from folder.models import Folder


# Create your models here.
class Task(models.Model):
    date = models.DateTimeField(default=datetime.now)
    name = models.TextField(max_length=50, default="Task Name")
    notes = models.TextField(max_length=500, default="", blank=True)
    status = models.TextField(max_length=50, default="pending")
    folder_id = models.ForeignKey(Folder, related_name="tasks", on_delete=models.CASCADE, default='')

