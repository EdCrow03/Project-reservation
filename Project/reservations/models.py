# reservations/models.py
from django.db import models
from authentification.models import Utilisateur
from django.urls import reverse

class Reservation(models.Model):
    TABLE_TYPE_CHOICES = [
        ('regular', 'Régulière'),
        ('vip', 'VIP'),
    ]
    
    TIME_CHOICES = [
        ('Breakfast', 'Petit-Déjeuner'),
        ('Lunch', 'Déjeuner'),
        ('Dinner', 'Dîner'),
    ]

    STATUS_CHOICES = [
        ('confirmed', 'Confirmée'),
        ('pending', 'En attente'),
        ('declined', 'Refusée'),
    ]
    
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    table_type = models.CharField(max_length=10, choices=TABLE_TYPE_CHOICES, default="regular")
    reservation_date = models.DateField(default='2023-01-01')
    number_of_guests = models.PositiveIntegerField(default=1)
    reservation_time = models.CharField(max_length=10, choices=TIME_CHOICES, default="Breakfast")
    message = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"Réservation par {self.utilisateur.nom_et_prenom} pour {self.reservation_date} à {self.reservation_time}"

    def get_absolute_url(self):
        return reverse('reservations:edit_reservation', args=[str(self.id)])

    def get_delete_url(self):
        return reverse('reservations:delete_reservation', args=[str(self.id)])