# Generated by Django 3.1.2 on 2020-10-27 16:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_auto_20201022_2154'),
        ('slots', '0007_slot_book_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slot',
            name='book_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slots', to='books.book'),
        ),
    ]
