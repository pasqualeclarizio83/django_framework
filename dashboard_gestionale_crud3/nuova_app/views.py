from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from django.views.generic.detail import DetailView

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator

from django.http import JsonResponse, HttpResponse

import json
from requests.exceptions import HTTPError

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


# views.py
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Deposito

class DepositoListView(ListView):
    model = Deposito
    template_name = 'nuova_app/deposito_list.html'

class DepositoCreateView(CreateView):
    model = Deposito
    template_name = 'nuova_app/deposito_form.html'
    fields = ['loc_deposito', 'descrizione']
    success_url = reverse_lazy('deposito_list')

class DepositoUpdateView(UpdateView):
    model = Deposito
    template_name = 'nuova_app/deposito_form.html'
    fields = ['loc_deposito', 'descrizione']
    success_url = reverse_lazy('deposito_list')

class DepositoDeleteView(DeleteView):
    model = Deposito
    template_name = 'nuova_app/deposito_confirm_delete.html'
    success_url = reverse_lazy('deposito_list')