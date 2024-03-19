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

# CORSO
    
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from .models import Corso
from .forms import CorsoForm

class GestioneCorsiView(View):
    template_name = 'nuova_app/gestione_corsi.html'

    def get(self, request):
        corsi = Corso.objects.all()
        return render(request, self.template_name, {'corsi': corsi})

class CreaCorsoView(View):
    template_name = 'nuova_app/crea_corso.html'

    def get(self, request):
        form = CorsoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = CorsoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestione_corsi')
        return render(request, self.template_name, {'form': form})

class ModificaCorsoView(View):
    template_name = 'nuova_app/modifica_corso.html'

    def get(self, request, pk):
        corso = get_object_or_404(Corso, pk=pk)
        form = CorsoForm(instance=corso)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        corso = get_object_or_404(Corso, pk=pk)
        form = CorsoForm(request.POST, instance=corso)
        if form.is_valid():
            form.save()
            return redirect('gestione_corsi')
        return render(request, self.template_name, {'form': form})

class CancellaCorsoView(View):
    def post(self, request, pk):
        corso = get_object_or_404(Corso, pk=pk)
        corso.delete()
        return redirect('gestione_corsi')
    
# PROFESSORE
    
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from .models import Professore
from .forms import ProfessoreForm

class GestioneProfessoriView(View):
    template_name = 'nuova_app/gestione_professori.html'

    def get(self, request):
        professori = Professore.objects.all()
        return render(request, self.template_name, {'professori': professori})

class CreaProfessoreView(View):
    template_name = 'nuova_app/crea_professore.html'

    def get(self, request):
        form = ProfessoreForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ProfessoreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('gestione_professori')
        return render(request, self.template_name, {'form': form})

class ModificaProfessoreView(View):
    template_name = 'nuova_app/modifica_professore.html'

    def get(self, request, pk):
        professore = get_object_or_404(Professore, pk=pk)
        form = ProfessoreForm(instance=professore)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        professore = get_object_or_404(Professore, pk=pk)
        form = ProfessoreForm(request.POST, instance=professore)
        if form.is_valid():
            form.save()
            return redirect('gestione_professori')
        return render(request, self.template_name, {'form': form})

class CancellaProfessoreView(View):
    def post(self, request, pk):
        professore = get_object_or_404(Professore, pk=pk)
        professore.delete()
        return redirect('gestione_professori')


# STUDENTE

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from .models import Studente
from .forms import StudenteForm

class ListaStudentiView(View):
    template_name = 'nuova_app/lista_studenti.html'

    def get(self, request):
        studenti = Studente.objects.all()
        return render(request, self.template_name, {'studenti': studenti})

class CreaStudenteView(View):
    template_name = 'nuova_app/crea_studente.html'

    def get(self, request):
        form = StudenteForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = StudenteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_studenti'))
        return render(request, self.template_name, {'form': form})

class ModificaStudenteView(View):
    template_name = 'nuova_app/modifica_studente.html'

    def get(self, request, pk):
        studente = get_object_or_404(Studente, pk=pk)
        form = StudenteForm(instance=studente)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        studente = get_object_or_404(Studente, pk=pk)
        form = StudenteForm(request.POST, instance=studente)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_studenti'))
        return render(request, self.template_name, {'form': form})

class CancellaStudenteView(View):
    template_name = 'nuova_app/conferma_cancellazione_studente.html'

    def get(self, request, pk):
        studente = get_object_or_404(Studente, pk=pk)
        return render(request, self.template_name, {'studente': studente})

    def post(self, request, pk):
        studente = get_object_or_404(Studente, pk=pk)
        studente.delete()
        return redirect(reverse('lista_studenti'))


# INSEGNAMENTO

from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.urls import reverse
from .models import Insegnamento
from .forms import InsegnamentoForm

class ListaInsegnamentiView(View):
    template_name = 'nuova_app/lista_insegnamenti.html'

    def get(self, request):
        insegnamenti = Insegnamento.objects.all()
        return render(request, self.template_name, {'insegnamenti': insegnamenti})

class CreaInsegnamentoView(View):
    template_name = 'nuova_app/crea_insegnamento.html'

    def get(self, request):
        form = InsegnamentoForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = InsegnamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_insegnamenti'))
        return render(request, self.template_name, {'form': form})

class ModificaInsegnamentoView(View):
    template_name = 'nuova_app/modifica_insegnamento.html'

    def get(self, request, pk):
        insegnamento = get_object_or_404(Insegnamento, pk=pk)
        form = InsegnamentoForm(instance=insegnamento)
        return render(request, self.template_name, {'form': form})

    def post(self, request, pk):
        insegnamento = get_object_or_404(Insegnamento, pk=pk)
        form = InsegnamentoForm(request.POST, instance=insegnamento)
        if form.is_valid():
            form.save()
            return redirect(reverse('lista_insegnamenti'))
        return render(request, self.template_name, {'form': form})

class CancellaInsegnamentoView(View):
    template_name = 'nuova_app/conferma_cancellazione_insegnamento.html'

    def get(self, request, pk):
        insegnamento = get_object_or_404(Insegnamento, pk=pk)
        return render(request, self.template_name, {'insegnamento': insegnamento})

    def post(self, request, pk):
        insegnamento = get_object_or_404(Insegnamento, pk=pk)
        insegnamento.delete()
        return redirect(reverse('lista_insegnamenti'))

    
