# Generated by Django 3.1.2 on 2021-01-21 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Templates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField(blank=True, default='')),
                ('name', models.TextField(blank=True, default='', max_length=50)),
                ('body', models.TextField(blank=True, default='')),
            ],
        ),
    ]