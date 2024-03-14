from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

from django.views.generic.detail import DetailView

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.core.paginator import Paginator

from django.http import JsonResponse, HttpResponse

import json
from requests.exceptions import HTTPError

import csv
from .models import Deposito, Articoli


from django.db import connection

import csv
from collections import defaultdict


def controlla_depositi_doppi(nome_file):
    depositi_doppi = []
    depositi_visti = defaultdict(int)

    with open(nome_file, 'r', newline='', encoding='utf-8') as file_csv:
        lettore = csv.reader(file_csv)
        next(lettore)  # Salta l'intestazione del file CSV
        for riga in lettore:
            ditta, codice, deposito = riga
            depositi_visti[deposito] += 1

    for deposito, conteggio in depositi_visti.items():
        if conteggio > 1:
            depositi_doppi.append(deposito)

    return depositi_doppi

def importa_depositi_da_csv(nome_file):
    depositi_doppi = controlla_depositi_doppi(nome_file)
    if depositi_doppi:
        print("Ci sono depositi duplicati:", depositi_doppi)
        return

    with open(nome_file, 'r', newline='', encoding='utf-8') as file_csv:
        lettore = csv.reader(file_csv)
        next(lettore)  # Salta l'intestazione del file CSV
        for riga in lettore:
            ditta, codice, deposito = riga
            descrizione = f"vengo dal {deposito}"
            Deposito.objects.create(loc_deposito=deposito, descrizione=descrizione)


def truncate_table(table_name):
    with connection.cursor() as cursor:
        cursor.execute(f'TRUNCATE TABLE {table_name};')






# la procedura permette di esportare
# i dati dal CSV e salvarli
# popolando le tabelle
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



import pandas as pd

def popola_articoli_da_csv(nome_file):
    # Leggi il file CSV utilizzando pandas
    df = pd.read_csv(nome_file, delimiter=';')
    
    # Rimuovi eventuali duplicati dal DataFrame
    df.drop_duplicates(subset=['CODICE'], keep='first', inplace=True)
    
    # Itera sul DataFrame per popolare il modello Articoli
    for index, row in df.iterrows():
        codice = row['CODICE']
        descrizione = row['DESCRIZIONE']
        
        # Verifica se il codice esiste già nel database
        if not Articoli.objects.filter(codice=codice).exists():
            # Crea un nuovo oggetto Articoli
            Articoli.objects.create(codice=codice, descrizione=descrizione)
            print(f"Creato articolo: {codice}")
        else:
            print(f"Il codice {codice} esiste già")



class HomeVuota(View): # è vuota
    def get(self, request, *args, **kwargs):
        try:
            # Utilizzo
            # Utilizzo
            # popola_tabella_deposito_da_csv('Giacenze.csv')
            # popola_articoli_da_csv('Articoli.csv')
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



from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Articoli

from django.views.generic import DetailView

from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Articoli
from .forms import ArticoliForm

class VisualizzaArticoli(ListView):
    model = Articoli
    template_name = 'nuova_app/visualizza_articoli.html'

class CreaArticolo(CreateView):
    model = Articoli
    form_class = ArticoliForm
    template_name = 'nuova_app/crea_articolo.html'
    success_url = reverse_lazy('visualizza_articoli')

class ModificaArticolo(UpdateView):
    model = Articoli
    form_class = ArticoliForm
    template_name = 'nuova_app/modifica_articolo.html'
    success_url = reverse_lazy('visualizza_articoli')

class CancellaArticolo(DeleteView):
    model = Articoli
    template_name = 'nuova_app/cancella_articolo.html'
    success_url = reverse_lazy('visualizza_articoli')