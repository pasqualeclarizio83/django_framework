from django.shortcuts import render
from .models import Articolo
from django.views.generic import ListView, DetailView

class ArticoliView(ListView):
    model = Articolo
    template_name = "applicazione/pagina.html"
    context_object_name = 'articoli'
    paginate_by = 25