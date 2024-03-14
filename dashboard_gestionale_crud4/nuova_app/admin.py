from django.contrib import admin

from .models import *

class AdminDeposito(admin.ModelAdmin):
    model = Deposito
    list_display = ("pk", "loc_deposito", "descrizione")
    search_fields = ["loc_deposito", 'descrizione']

class AdminArticolo(admin.ModelAdmin):
    model = Articoli
    list_display = ("pk", "codice", "descrizione")
    search_fields = ["codice", 'descrizione']

# popolare il Deposito
admin.site.register(Deposito, AdminDeposito)
# popolare Articoli
admin.site.register(Articoli, AdminArticolo)
