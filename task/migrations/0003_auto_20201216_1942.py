# Generated by Django 3.1.2 on 2020-12-16 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('folder', '0004_remove_folder_tasks'),
        ('task', '0002_auto_20201216_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='folder_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to='folder.folder'),
        ),
    ]
