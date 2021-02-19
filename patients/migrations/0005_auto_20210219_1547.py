# Generated by Django 3.1.2 on 2021-02-19 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0004_oktainterview_okta_groups'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(default='', max_length=100, null=True)),
                ('lastName', models.CharField(default='', max_length=100, null=True)),
                ('ssn', models.CharField(default='', max_length=8, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='OktaInterview',
        ),
    ]
