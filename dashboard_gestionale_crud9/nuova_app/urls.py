from django.urls import path

from .views import (
    
    HomeVuota,

)

from . import views

urlpatterns = [
    # ORDINE
    # base1.html  homepage
    path("", HomeVuota.as_view(), name="homepage"), #1° PRIMO # pagina1.html

    path('dipartimenti/', views.lista_dipartimenti, name='lista_dipartimenti'),
    path('dipartimenti/<int:dipartimento_id>/', views.dettaglio_dipartimento, name='dettaglio_dipartimento'),
#
]