# Generated by Django 3.1.2 on 2021-02-13 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_apps', '0008_auto_20210213_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobapp',
            name='date_applied',
            field=models.DateField(default=datetime.date.today, null=True),
        ),
    ]
