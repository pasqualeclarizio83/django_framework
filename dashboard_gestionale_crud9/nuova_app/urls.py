from django.urls import path

from .views import (
    
    HomeVuota,

    ListaFacoltaView, CreaFacoltaView, ModificaFacoltaView, CancellaFacoltaView,

    GestioneCorsiView,

    # Professori

    GestioneProfessoriView, CreaProfessoreView, ModificaProfessoreView, CancellaProfessoreView,

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

    # CORSI

    path('corsi/', views.GestioneCorsiView.as_view(), name='gestione_corsi'),
    path('corsi/crea/', views.CreaCorsoView.as_view(), name='crea_corso'),
    path('corsi/modifica/<int:pk>/', views.ModificaCorsoView.as_view(), name='modifica_corso'),
    path('corsi/cancella/<int:pk>/', views.CancellaCorsoView.as_view(), name='cancella_corso'),

    # Professori

    path('professori/', GestioneProfessoriView.as_view(), name='gestione_professori'),
    path('professori/crea/', CreaProfessoreView.as_view(), name='crea_professore'),
    path('professori/modifica/<int:pk>/', ModificaProfessoreView.as_view(), name='modifica_professore'),
    path('professori/cancella/<int:pk>/', CancellaProfessoreView.as_view(), name='cancella_professore'),
#
]