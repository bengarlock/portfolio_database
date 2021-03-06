# Generated by Django 3.1.2 on 2020-12-16 19:41

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0004_remove_folder_tasks'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.TextField(default=datetime.date(2020, 12, 16), max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='folder_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='folder.folder'),
        ),
    ]
