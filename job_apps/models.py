from django.contrib.postgres.fields import ArrayField
from django.db import models
from datetime import date
from django.contrib.auth.models import User


class Jobapp(models.Model):
    company_name = models.TextField(default='', max_length=50, blank=True)
    job_title = models.TextField(default='', max_length=50, blank=True)
    url = models.TextField(default='', blank=True)
    technologies = ArrayField(models.CharField(max_length=255), default=list, blank=True)
    date_applied = models.DateField(null=True, default=date.today)
    status = models.TextField(default="Applied", max_length=50, blank=True)
    contact = models.TextField(default="Hiring Manager", blank=True)
    owner = models.ForeignKey(User, related_name="job_app", on_delete=models.CASCADE, null=True)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)
