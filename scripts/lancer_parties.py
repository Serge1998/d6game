# scripts/lancer_parties.py

import os
import sys
import time
import django
from django.core.management import call_command

# Chemin absolu vers le répertoire racine du projet (où se trouve manage.py)
PROJET_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configuration de l'environnement Django
sys.path.append(PROJET_DIR)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "d6game.settings")

# Setup Django
django.setup()

def main():
    print("🚀 Démarrage du script d'automatisation des parties...")
    while True:
        print("🔄 Génération d'une nouvelle partie...")
        call_command('generer_partie')
        time.sleep(120)  # Attend 60 secondes avant de générer une nouvelle partie

if __name__ == "__main__":
    main()