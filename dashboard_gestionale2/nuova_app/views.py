from django.shortcuts import render, redirect

from django.views import View

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.core.paginator import Paginator

from django.http import JsonResponse, HttpResponse


import json
from requests.exceptions import HTTPError

from .models import Anagrafica

class HomeVuota(View): # è vuota
    def get(self, request, *args, **kwargs):
        try:
            #popola_interessi("tv")
            a = {}
            context = {
                
                "provincia_dati": a
            }
            return render(request, "nuova_app/pagina1.html", context)
        except Exception as e:
            print (e)


# GESTISCO ANAGRAFICA


from .forms import AnagraficaForm

def anagrafica(request):
    # se devo gestire il GET
    if request.method == "GET":
        form = AnagraficaForm()
        return render(request, "nuova_app/anagrafica_form.html", {'anagrafica_form': form})
    else:
        # se devo gestire il POST
        form = AnagraficaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("anagrafica")

# LEGGI ANAGRAFICA
def lista_anagrafiche(request):
    anagrafiche = Anagrafica.objects.all()
    return render(request, 'nuova_app/mostra_lista.html', {'anagrafiche': anagrafiche})