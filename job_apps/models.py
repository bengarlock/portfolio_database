from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import date
from django.utils import timezone

class Jobapp(models.Model):
    company_name = models.TextField(default='', max_length=50, blank=True)
    job_title = models.TextField(default='', max_length=50, blank=True)
    url = models.TextField(default='', blank=True)
    technologies = ArrayField(models.CharField(max_length=255), default=list, blank=True)
    date_applied = models.DateField(default=timezone.now())
    status = models.TextField(default="Applied", max_length=50, blank=True)
    contact = models.TextField(default="Hiring Manager", blank=True)
    