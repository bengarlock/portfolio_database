# Generated by Django 3.1.2 on 2020-12-16 19:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0003_folder_tasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='folder',
            name='tasks',
        ),
    ]
