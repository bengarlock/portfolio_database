# Generated by Django 3.1.2 on 2020-10-31 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0003_auto_20201031_1048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='reservation_id',
        ),
    ]
