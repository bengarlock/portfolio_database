# Generated by Django 3.1.2 on 2021-02-19 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0005_auto_20210219_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patients',
            name='ssn',
            field=models.CharField(default='', max_length=50, null=True),
        ),
    ]