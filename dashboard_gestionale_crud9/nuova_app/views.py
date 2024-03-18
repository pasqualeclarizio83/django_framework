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


# inizia a gestirmi in base alle Classi

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Dipartimento

class ListaDipartimentiView(ListView):
    model = Dipartimento
    template_name = 'nuova_app/lista_dipartimenti.html'
    context_object_name = 'dipartimenti'

class DettaglioDipartimentoView(DetailView):
    model = Dipartimento
    template_name = 'nuova_app/dettaglio_dipartimento.html'
    context_object_name = 'dipartimento'

class CreazioneDipartimentoView(CreateView):
    model = Dipartimento
    template_name = 'nuova_app/creazione_dipartimento.html'
    fields = ['nome']
    success_url = reverse_lazy('lista_dipartimenti')

class ModificaDipartimentoView(UpdateView):
    model = Dipartimento
    template_name = 'nuova_app/modifica_dipartimento.html'
    fields = ['nome']
    success_url = reverse_lazy('lista_dipartimenti')

class CancellaDipartimentoView(DeleteView):
    model = Dipartimento
    template_name = 'nuova_app/conferma_cancellazione_dipartimento.html'
    success_url = reverse_lazy('lista_dipartimenti')
