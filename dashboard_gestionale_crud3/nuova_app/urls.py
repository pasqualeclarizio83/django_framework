from django.urls import path

from .views import (
    
    HomeVuota,

    DepositoListView,

    DepositoCreateView,

    DepositoUpdateView,

    DepositoDeleteView,

)

urlpatterns = [
    # ORDINE
    # base1.html  homepage
    path("", HomeVuota.as_view(), name="homepage"), #1° PRIMO # pagina1.html

    path('depositi/', DepositoListView.as_view(), name='deposito_list'),

    path('add/', DepositoCreateView.as_view(), name='deposito_add'),

    path('<int:pk>/edit/', DepositoUpdateView.as_view(), name='deposito_edit'),
    path('<int:pk>/delete/', DepositoDeleteView.as_view(), name='deposito_delete'),

]