# Generated by Django 3.1.2 on 2020-11-03 11:35

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guests', '0003_auto_20201027_2242'),
    ]

    operations = [
        migrations.AddField(
            model_name='guest',
            name='slots',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=15), blank=True, default=list, size=None),
        ),
    ]
