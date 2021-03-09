from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.


class Patient(models.Model):
    first_name = models.CharField(default='', max_length=100, null=True)
    last_name = models.CharField(default='', max_length=100, null=True)
    ssn = models.CharField(default='', max_length=50, null=True)
    member_id = models.CharField(default='', max_length=50, null=True)
    medical_records = ArrayField(models.CharField(max_length=15), default=list, blank=True)
    plan_benefit_info = ArrayField(models.CharField(max_length=15), default=list, blank=True)
    email = models.CharField(default='', max_length=50, null=True)

class Prescriptions(models.Model):
    name = models.CharField(default='', max_length=50, null=True)
    doctor = models.CharField(default='', max_length=50, null=True)
    patient_id = models.ForeignKey(Patient, related_name="prescriptions", on_delete=models.SET_NULL, null=True)


