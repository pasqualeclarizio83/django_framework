from django import forms

from .models import Facolta

class FacoltaForm(forms.ModelForm):
    class Meta:
        model = Facolta
        fields = ['nome', 'dipartimento']

# CORSO
        
from django import forms
from .models import Corso

class CorsoForm(forms.ModelForm):
    class Meta:
        model = Corso
        fields = ['nome', 'facolta']

# Professore Form
        
from django import forms
from .models import Professore

class ProfessoreForm(forms.ModelForm):
    class Meta:
        model = Professore
        fields = ['nome', 'cognome', 'facolta']

# STUDENTE
        
from .models import Studente
        
class StudenteForm(forms.ModelForm):
    class Meta:
        model = Studente
        fields = ['nome', 'cognome', 'corso_di_laurea']

# Insegnamento
        
from django import forms
from .models import Insegnamento

class InsegnamentoForm(forms.ModelForm):
    class Meta:
        model = Insegnamento
        fields = ['nome', 'professore', 'corso']

# iscrizione

from django import forms
from .models import Iscrizione

class IscrizioneForm(forms.ModelForm):
    class Meta:
        model = Iscrizione
        fields = ['studente', 'insegnamento']