from django.shortcuts import render
from django.http import HttpResponse
from .models import Giornalista, Articolo
# Create your views here.
def home(request):
  a = ""
  g = ""
  for art in Articolo.objects.all():
    a += (art.titolo)

  for gio in Giornalista.objects.all():
    g += (gio.nome + " " + gio.cognome)

  response = "Articoli: " + a + " Giornalisti: " + g
  print(response)
  return HttpResponse(response) 