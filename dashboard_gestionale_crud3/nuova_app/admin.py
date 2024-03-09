from django.contrib import admin

from .models import *

class AdminAnagrafica(admin.ModelAdmin):
    model = Anagrafica
    list_display = ("pk", "nome", "cognome")
    search_fields = ["nome", 'descrizione']

admin.site.register(Anagrafica, AdminAnagrafica)
