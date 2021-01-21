from django.db import models

class Templates(models.Model):
    type = models.TextField(default='', blank=True)
    name = models.TextField(default='', max_length=50, blank=True)
    body = models.TextField(default='', blank=True)

