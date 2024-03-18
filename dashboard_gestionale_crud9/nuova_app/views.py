from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

class HomeVuota(View): # è vuota
    def get(self, request, *args, **kwargs):
        try:
            a = {}
            context = {
                
                "provincia_dati": a
            }
            return render(request, "nuova_app/pagina1.html", context)
        except Exception as e:
            print (e)

# Inizio a gestirmi le Views
            
from django.shortcuts import render
from .models import Dipartimento, Facolta, Corso, Professore, Studente, Insegnamento, Iscrizione

def lista_dipartimenti(request):
    dipartimenti = Dipartimento.objects.all()
    return render(request, 'nuova_app/lista_dipartimenti.html', {'dipartimenti': dipartimenti})

def dettaglio_dipartimento(request, dipartimento_id):
    dipartimento = Dipartimento.objects.get(id=dipartimento_id)
    return render(request, 'nuova_app/dettaglio_dipartimento.html', {'dipartimento': dipartimento})