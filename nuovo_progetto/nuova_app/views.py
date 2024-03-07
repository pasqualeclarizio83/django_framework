from django.shortcuts import render, redirect

from django.views import View

from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from django.core.paginator import Paginator

from django.http import JsonResponse, HttpResponse


import json
from requests.exceptions import HTTPError

class HomeVuota(View): # è vuota
    def get(self, request, *args, **kwargs):
        try:
            #popola_interessi("tv")
            a = {}
            context = {
                
                "provincia_dati": a
            }
            return render(request, "nuova_app/pagina1.html", context)
        except Exception as e:
            print (e)