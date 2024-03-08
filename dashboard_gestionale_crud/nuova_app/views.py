from django.shortcuts import render, redirect

from django.views import View

from django.views.generic.detail import DetailView

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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

# Anagrafica con la Classe
class AnagraficaListView(ListView):
    model = Anagrafica
    template_name = 'nuova_app/mostra_lista.html'
    context_object_name = 'anagrafiche'

# Dettaglio Anagrafica

class AnagraficaDetailView(DetailView):
    model = Anagrafica
    template_name = 'nuova_app/dettaglio_anagrafica.html'
    context_object_name = 'anagrafica'

# Crea
    
from django.urls import reverse_lazy

class AnagraficaCreateView(CreateView):
    model = Anagrafica
    template_name = 'crea_anagrafica.html'
    fields = ['nome', 'cognome']
    success_url = reverse_lazy('mostra_lista')


# CRUD
    
class AnagraficaUpdateView(UpdateView):
    model = Anagrafica
    template_name = 'nuova_app/modifica_anagrafica.html'
    fields = ['nome', 'cognome']
    success_url = reverse_lazy('lista_anagrafiche')

class AnagraficaDeleteView(DeleteView):
    model = Anagrafica
    template_name = 'nuova_app/elimina_anagrafica.html'
    success_url = reverse_lazy('lista_anagrafiche')