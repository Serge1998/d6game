# game/management/commands/generer_partie.py

import random
from django.core.management.base import BaseCommand
from game.models import Partie

class Command(BaseCommand):
    help = 'Génère une nouvelle partie automatiquement'

    def handle(self, *args, **kwargs):
        from datetime import datetime
        self.stdout.write(f'[{datetime.now()}] Génération d’une nouvelle partie...')
        joueur_tour1 = random.randint(2, 12)
        joueur_tour2 = random.randint(2, 12)
        croupier_tour1 = random.randint(2, 12)
        croupier_tour2 = random.randint(2, 12)

        Partie.objects.create(
            joueur_tour1=joueur_tour1,
            joueur_tour2=joueur_tour2,
            croupier_tour1=croupier_tour1,
            croupier_tour2=croupier_tour2
        )
        self.stdout.write(self.style.SUCCESS('✅ Partie créée avec succès !'))