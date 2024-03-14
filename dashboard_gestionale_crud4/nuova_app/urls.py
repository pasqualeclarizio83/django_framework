from django.urls import path

from .views import (
    
    HomeVuota,

    DepositoListView,

    DepositoCreateView,

    DepositoUpdateView,

    DepositoDeleteView,

    VisualizzaArticoli, 
    
    CreaArticolo, 
    
    ModificaArticolo, 
    
    CancellaArticolo

)

urlpatterns = [
    # ORDINE
    # base1.html  homepage
    path("", HomeVuota.as_view(), name="homepage"), #1° PRIMO # pagina1.html

    path('depositi/', DepositoListView.as_view(), name='deposito_list'),

    path('add/', DepositoCreateView.as_view(), name='deposito_add'),

    path('<int:pk>/edit/', DepositoUpdateView.as_view(), name='deposito_edit'),
    path('<int:pk>/delete/', DepositoDeleteView.as_view(), name='deposito_delete'),


    path('visualizza_articoli/', VisualizzaArticoli.as_view(), name='visualizza_articoli'),
    path('crea/', CreaArticolo.as_view(), name='crea_articolo'),
    path('modifica/<int:pk>/', ModificaArticolo.as_view(), name='modifica_articolo'),
    path('cancella/<int:pk>/', CancellaArticolo.as_view(), name='cancella_articolo'),
#
]