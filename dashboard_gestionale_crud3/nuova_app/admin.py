from django.contrib import admin

from .models import *

class AdminDeposito(admin.ModelAdmin):
    model = Deposito
    list_display = ("pk", "loc_deposito", "descrizione")
    search_fields = ["loc_deposito", 'descrizione']

# popolare il Deposito
admin.site.register(Deposito, AdminDeposito)
