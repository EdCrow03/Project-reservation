# Generated by Django 5.0.6 on 2024-06-30 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateField(default='2023-01-01'),
        ),
    ]
