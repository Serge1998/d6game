from django.db import models

# Create your models here.
from django.db import models
import random
from django.utils import dateformat

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name="Téléphone")
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name="Pays")

# Créer automatiquement un profil à l'inscription
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

post_save.connect(create_profile, sender=User)




def lancer_des():
    return random.randint(1, 6) + random.randint(1, 6)

class Partie(models.Model):
    numero = models.PositiveIntegerField(unique=True)
    joueur_tour1 = models.PositiveIntegerField()
    joueur_tour2 = models.PositiveIntegerField()
    croupier_tour1 = models.PositiveIntegerField()
    croupier_tour2 = models.PositiveIntegerField()
    date_debut = models.DateTimeField(auto_now_add=True)
    date_fin = models.DateTimeField(auto_now=True)

    @property
    def joueur_total(self):
        return self.joueur_tour1 + self.joueur_tour2


    @property
    def date_fin_formattee(self):
        return dateformat.format(self.date_fin, 'd/m/Y H:i:s')

    @property
    def croupier_total(self):
        return self.croupier_tour1 + self.croupier_tour2

    @property
    def gagnant(self):
        if self.joueur_total > self.croupier_total:
            return "Joueur"
        elif self.croupier_total > self.joueur_total:
            return "Croupier"
        else:
            return "Égalité"

    def save(self, *args, **kwargs):
        if not self.numero:
            dernier = Partie.objects.order_by('-numero').first()
            self.numero = 1 if not dernier else dernier.numero + 1
        super().save(*args, **kwargs)