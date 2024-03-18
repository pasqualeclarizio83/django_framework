from django.shortcuts import render, redirect, get_object_or_404

from django.views import View

class HomeVuota(View): # è vuota
    def get(self, request, *args, **kwargs):
        try:
            a = {}
            context = {
                
                "provincia_dati": a
            }
            return render(request, "nuova_app/pagina1.html", context)
        except Exception as e:
            print (e)


# inizia a gestirmi in base alle Classi

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Dipartimento

class ListaDipartimentiView(ListView):
    model = Dipartimento
    template_name = 'nuova_app/lista_dipartimenti.html'
    context_object_name = 'dipartimenti'

class DettaglioDipartimentoView(DetailView):
    model = Dipartimento
    template_name = 'nuova_app/dettaglio_dipartimento.html'
    context_object_name = 'dipartimento'

class CreazioneDipartimentoView(CreateView):
    model = Dipartimento
    template_name = 'nuova_app/creazione_dipartimento.html'
    fields = ['nome']
    success_url = reverse_lazy('lista_dipartimenti')

class ModificaDipartimentoView(UpdateView):
    model = Dipartimento
    template_name = 'nuova_app/modifica_dipartimento.html'
    fields = ['nome']
    success_url = reverse_lazy('lista_dipartimenti')

class CancellaDipartimentoView(DeleteView):
    model = Dipartimento
    template_name = 'nuova_app/conferma_cancellazione_dipartimento.html'
    success_url = reverse_lazy('lista_dipartimenti')


# FACOLTA

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Facolta
from .forms import FacoltaForm

class ListaFacoltaView(View):
    template_name = 'nuova_app/lista_facolta.html'

    def get(self, request):
        print ("leggi Facolta")
        facolta = Facolta.objects.all()
        return render(request, self.template_name, {'facolta': facolta})

class CreaFacoltaView(View):
    template_name = 'nuova_app/crea_facolta.html'

    def get(self, request):
        print ("Sono nel get di Crea Facolta")
        form = FacoltaForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = FacoltaForm(request.POST)
        if form.is_valid():
            print ("Creazione del Post")
            form.save()
            return redirect('lista_facolta')
        return render(request, self.template_name, {'form': form})

class ModificaFacoltaView(View):
    template_name = 'nuova_app/modifica_facolta.html'

    def get(self, request, pk):
        facolta = get_object_or_404(Facolta, pk=pk)
        form = FacoltaForm(instance=facolta)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        print ("Modifica del Post")
        facolta = get_object_or_404(Facolta, pk=pk)
        form = FacoltaForm(request.POST, instance=facolta)
        if form.is_valid():
            form.save()
            return redirect('lista_facolta')
        return render(request, self.template_name, {'form': form})

class CancellaFacoltaView(View):
    def post(self, request, pk):
        print ("Cancella Post")
        facolta = get_object_or_404(Facolta, pk=pk)
        facolta.delete()
        return redirect('lista_facolta')
