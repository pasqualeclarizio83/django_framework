from django.urls import path

from .views import (
    
    HomeVuota,

    DepositoListView,

)

urlpatterns = [
    # ORDINE
    # base1.html  homepage
    path("", HomeVuota.as_view(), name="homepage"), #1° PRIMO # pagina1.html

    path('depositi/', DepositoListView.as_view(), name='deposito_list'),

]