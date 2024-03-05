from .models import Autore, Libro
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

class AutoreDetailCBV(DetailView):
    model = Autore
    template_name = "autore.html"

class LibroListCBV(ListView):
    model = Libro
    template_name = "lista_libri.html"
