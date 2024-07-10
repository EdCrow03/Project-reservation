from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

# Create your models here.
class Utilisateur(models.Model):
    nom_et_prenom = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    date_naissance = models.DateField()
    numero_telephone = models.CharField(max_length=15)
    is_staff = models.BooleanField(default=False)

    def __str__(self):
        return self.nom_et_prenom

    def save(self, *args, **kwargs):
        if not self.id:
            self.password = make_password(self.password)
        super(Utilisateur, self).save(*args, **kwargs)

    def verify_password(self, raw_password):
        return check_password(raw_password, self.password)