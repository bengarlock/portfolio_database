# Generated by Django 3.1.2 on 2021-03-09 19:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0012_auto_20210309_1923'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='prescriptions',
        ),
        migrations.AddField(
            model_name='prescriptions',
            name='patient_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prescriptions', to='patients.patient'),
        ),
    ]
