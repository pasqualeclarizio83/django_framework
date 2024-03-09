from django.shortcuts import render, redirect, get_object_or_404

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

# CRUD
    
from django.urls import reverse_lazy
# Anagrafica Form
from .forms import AnagraficaForm

class AnagraficaListView(View):
    def get(self, request):
        anagrafiche = Anagrafica.objects.all()
        return render(request, 'nuova_app/anagrafica_list.html', {'anagrafiche': anagrafiche})

class AnagraficaCreateView(View):
    def post(self, request):
        form = AnagraficaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anagrafica_list')
        return render(request, 'nuova_app/anagrafica_form.html', {'form': form})

    def get(self, request):
        form = AnagraficaForm()
        return render(request, 'nuova_app/anagrafica_form.html', {'form': form})

class AnagraficaUpdateView(View):
    def post(self, request, pk):
        anagrafica = get_object_or_404(Anagrafica, pk=pk)
        form = AnagraficaForm(request.POST, instance=anagrafica)
        if form.is_valid():
            form.save()
            return redirect('anagrafica_list')
        return render(request, 'nuova_app/anagrafica_modifica.html', {'form': form})

    def get(self, request, pk):
        anagrafica = get_object_or_404(Anagrafica, pk=pk)
        form = AnagraficaForm(instance=anagrafica)
        return render(request, 'nuova_app/anagrafica_modifica.html', {'form': form})

class AnagraficaDeleteView(DeleteView):
    model = Anagrafica
    success_url = reverse_lazy('anagrafica_list')