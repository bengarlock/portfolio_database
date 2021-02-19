from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class Patients(models.Model):
    firstName = models.CharField(default='', max_length=100, null=True)
    lastName = models.CharField(default='', max_length=100, null=True)
    ssn = models.CharField(default='', max_length=50, null=True)

