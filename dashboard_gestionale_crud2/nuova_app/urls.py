from django.urls import path

from .views import (
    
    HomeVuota, 
    
    AnagraficaCRUDView, # PER LE CRUD

)

urlpatterns = [
    # ORDINE
    # base1.html  homepage
    path("", HomeVuota.as_view(), name="homepage"), #1° PRIMO # pagina1.html

    path('anagrafica/', AnagraficaCRUDView.as_view(), name='anagrafica_list'),
    path('anagrafica/<int:pk>/delete/', AnagraficaCRUDView.as_view(), name='anagrafica_delete'),
    path('anagrafica/modifica/<int:pk>/', AnagraficaCRUDView.as_view(), name='anagrafica_modifica'),
    path('anagrafica/crea/', AnagraficaCRUDView.as_view(), name='anagrafica_crea'),
]