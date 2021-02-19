from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(default='', max_length=100, null=True)
    last_name = models.CharField(default='', max_length=100, null=True)
    ssn = models.CharField(default='', max_length=50, null=True)
