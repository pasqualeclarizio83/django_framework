from django.urls import path

from .views import (
    
    HomeVuota, 
    
    anagrafica, # anagrafica

    lista_anagrafiche, # Leggi anagrafica

)

urlpatterns = [
    # ORDINE
    # base1.html  homepage
    path("", HomeVuota.as_view(), name="homepage"), #1° PRIMO # pagina1.html

    path('anagrafica/', anagrafica, name='anagrafica'),

    path('anagrafiche/', lista_anagrafiche, name='lista_anagrafiche'),
]