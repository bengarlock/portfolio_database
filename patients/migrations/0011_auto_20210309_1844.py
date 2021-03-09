# Generated by Django 3.1.2 on 2021-03-09 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0010_auto_20210309_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='prescriptions',
        ),
        migrations.CreateModel(
            name='Prescriptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, null=True)),
                ('doctor', models.CharField(default='', max_length=50, null=True)),
                ('patient_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='prescriptions', to='patients.patient')),
            ],
        ),
    ]