from django.urls import path

from .views import (
    
    HomeVuota, 
    
    AnagraficaListView, AnagraficaCreateView, AnagraficaUpdateView, AnagraficaDeleteView

)

urlpatterns = [
    # ORDINE
    # base1.html  homepage
    path("", HomeVuota.as_view(), name="homepage"), #1° PRIMO # pagina1.html

    path('anagrafica/', AnagraficaListView.as_view(), name='anagrafica_list'),
    path('anagrafica/crea/', AnagraficaCreateView.as_view(), name='anagrafica_crea'),
    path('anagrafica/<int:pk>/modifica/', AnagraficaUpdateView.as_view(), name='anagrafica_modifica'),
    path('anagrafica/<int:pk>/cancella/', AnagraficaDeleteView.as_view(), name='anagrafica_cancella'),
    path('anagrafica/new_form/', AnagraficaCreateView.as_view(), name='anagrafica_new_form'),
]