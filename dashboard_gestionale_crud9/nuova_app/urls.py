from django.urls import path

from .views import (
    
    HomeVuota,

)

from . import views

urlpatterns = [
    # ORDINE
    # base1.html  homepage
    path("", HomeVuota.as_view(), name="homepage"), #1° PRIMO # pagina1.html

    path('dipartimenti/', views.ListaDipartimentiView.as_view(), name='lista_dipartimenti'),
    path('dipartimenti/<int:pk>/', views.DettaglioDipartimentoView.as_view(), name='dettaglio_dipartimento'),
    path('dipartimenti/crea/', views.CreazioneDipartimentoView.as_view(), name='crea_dipartimento'),
#
]