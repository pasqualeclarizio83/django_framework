from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from django.views.generic.detail import DetailView

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator

from django.http import JsonResponse, HttpResponse

import json
from requests.exceptions import HTTPError

import csv
from .models import Deposito

def popola_tabella_deposito_da_csv(file_path):
    # Apri il file CSV e leggi i dati
    with open(file_path, mode='r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            # Ottieni i dati dal CSV
            loc_deposito = row['DEPOSITO']
            descrizione = f"Deposito {loc_deposito}"
            
            # Crea un'istanza di Deposito e salvala nel database
            deposito, created = Deposito.objects.get_or_create(
                loc_deposito=loc_deposito,
                defaults={'descrizione': descrizione}
            )
            # Stampa le informazioni sulla creazione dell'istanza
            if created:
                print(f"Creato deposito: {loc_deposito}")
            else:
                print(f"Il deposito {loc_deposito} esiste già.")

            # Se vuoi assegnare altre informazioni al deposito, come DITTA, CODICE e GIACENZE,
            # puoi farlo qui.



class HomeVuota(View): # è vuota
    def get(self, request, *args, **kwargs):
        try:
            popola_tabella_deposito_da_csv('giacenze.csv')
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