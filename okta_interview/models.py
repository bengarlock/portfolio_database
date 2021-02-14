from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class OktaInterview(models.Model):
    firstName = models.CharField(default='', max_length=100, null=True)
    lastName = models.CharField(default='', max_length=100, null=True)
    mobilePhone = models.CharField(default='', max_length=100, null=True)
    displayName = models.CharField(default='', max_length=100, null=True)
    secondEmail = models.CharField(default='', max_length=100, null=True)
    login = models.CharField(default='', max_length=100, null=True)
    email = models.CharField(default='', max_length=100, null=True)
    oktaid = models.CharField(default='', max_length=100, null=True)
    okta_groups = ArrayField(models.CharField(max_length=15), default=list, blank=True)


