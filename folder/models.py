from django.db import models
from django.contrib.postgres.fields import ArrayField


class Folder(models.Model):
    name = models.TextField(default="", max_length=50)
