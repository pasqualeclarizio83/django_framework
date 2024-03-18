from django.urls import path

from .views import (
    
    HomeVuota,

    ListaFacoltaView, CreaFacoltaView, ModificaFacoltaView, CancellaFacoltaView

)

from . import views

urlpatterns = [
    # ORDINE
    # base1.html  homepage
    path("", HomeVuota.as_view(), name="homepage"), #1° PRIMO # pagina1.html

    path('dipartimenti/', views.ListaDipartimentiView.as_view(), name='lista_dipartimenti'),
    path('dipartimenti/<int:pk>/', views.DettaglioDipartimentoView.as_view(), name='dettaglio_dipartimento'),
    path('dipartimenti/crea/', views.CreazioneDipartimentoView.as_view(), name='crea_dipartimento'),
    path('dipartimenti/<int:pk>/modifica/', views.ModificaDipartimentoView.as_view(), name='modifica_dipartimento'),
    path('dipartimenti/<int:pk>/cancella/', views.CancellaDipartimentoView.as_view(), name='cancella_dipartimento'),

    # FACOLTA

    path('lista_facolta/', ListaFacoltaView.as_view(), name='lista_facolta'),
    path('crea/', CreaFacoltaView.as_view(), name='crea_facolta'),
    path('modifica/<int:pk>/', ModificaFacoltaView.as_view(), name='modifica_facolta'),
    path('cancella/<int:pk>/', CancellaFacoltaView.as_view(), name='cancella_facolta'),
#
]