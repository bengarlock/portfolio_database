# Generated by Django 3.1.2 on 2020-12-16 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20201216_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='notes',
            field=models.TextField(blank=True, default='', max_length=500),
        ),
    ]