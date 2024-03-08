from django.urls import path

from .views import (
    
    HomeVuota, 
    
    anagrafica, # anagrafica

    AnagraficaListView, # Leggi anagrafica

    AnagraficaUpdateView,

    AnagraficaDeleteView,

)

urlpatterns = [
    # ORDINE
    # base1.html  homepage
    path("", HomeVuota.as_view(), name="homepage"), #1° PRIMO # pagina1.html

    path('anagrafica/', anagrafica, name='anagrafica'),

    path('anagrafiche/', AnagraficaListView.as_view(), name='lista_anagrafiche'),
    path('anagrafiche/<int:pk>/', AnagraficaUpdateView.as_view(), name='modifica_anagrafica'),
    path('anagrafiche/<int:pk>/', AnagraficaDeleteView.as_view(), name='elimina_anagrafica'),
]