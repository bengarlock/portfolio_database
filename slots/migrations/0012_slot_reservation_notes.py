# Generated by Django 3.1.2 on 2020-10-28 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slots', '0011_auto_20201027_2240'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='reservation_notes',
            field=models.TextField(blank=True),
        ),
    ]
