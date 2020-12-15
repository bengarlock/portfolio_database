# Generated by Django 3.1.2 on 2020-10-31 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tables', '0002_auto_20201030_1925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='name',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='reservation_id',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.TextField(default='done'),
        ),
    ]
