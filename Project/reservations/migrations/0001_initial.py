# Generated by Django 5.0.6 on 2024-06-30 18:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentification', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('table_type', models.CharField(choices=[('regular', 'Régulière'), ('vip', 'VIP')], default='regular', max_length=10)),
                ('reservation_date', models.DateField()),
                ('number_of_guests', models.PositiveIntegerField(default=1)),
                ('reservation_time', models.CharField(choices=[('Breakfast', 'Petit-Déjeuner'), ('Lunch', 'Déjeuner'), ('Dinner', 'Dîner')], default='Breakfast', max_length=10)),
                ('message', models.TextField(blank=True, null=True)),
                ('utilisateur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentification.utilisateur')),
            ],
        ),
    ]
