from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Partie
import random
from django.utils import timezone
import time
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import RegisterForm  

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username} ! Vous pouvez maintenant vous connecter.')
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'game/register.html', {'form': form})



@login_required
def historique(request):
    return render(request, 'game/historique.html')



def index(request):
    derniere_partie = Partie.objects.order_by('-numero').first()
    maintenant = timezone.now()

    if not derniere_partie or (maintenant - derniere_partie.date_fin).seconds >= 60:
        # Générer les lancés par tour
        j1 = random.randint(2, 12)
        j2 = random.randint(2, 12)
        c1 = random.randint(2, 12)
        c2 = random.randint(2, 12)

        Partie.objects.create(
            joueur_tour1=j1,
            joueur_tour2=j2,
            croupier_tour1=c1,
            croupier_tour2=c2,
        )
        derniere_partie = Partie.objects.order_by('-numero').first()

    return render(request, 'game/index.html')




def historique(request):
    return render(request, 'game/historique.html')



def historique_ajax(request):
    parties = Partie.objects.all().order_by('-numero')[:10000]
    data = [
        {
            'numero': p.numero,
            'joueur_total': p.joueur_total,
            'croupier_total': p.croupier_total,
            'gagnant': p.gagnant,
            'date_fin': dateformat.format(p.date_fin, 'd/m/Y H:i:s')
        }
        for p in parties
    ]
    return JsonResponse(data, safe=False)


# game/views.py
from django.utils import dateformat

def derniere_partie_ajax(request):
    derniere = Partie.objects.order_by('-numero').first()
    if derniere:
        data = {
            'numero': derniere.numero,
            'joueur_tour1': derniere.joueur_tour1,
            'joueur_tour2': derniere.joueur_tour2,
            'croupier_tour1': derniere.croupier_tour1,
            'croupier_tour2': derniere.croupier_tour2,
            'joueur_total': derniere.joueur_total,
            'croupier_total': derniere.croupier_total,
            'gagnant': derniere.gagnant,
            'date_fin': dateformat.format(derniere.date_fin, 'd/m/Y H:i:s'),
        }
    else:
        data = {}

    return JsonResponse(data)