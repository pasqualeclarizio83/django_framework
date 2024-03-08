from django import forms
from .models import Anagrafica

class AnagraficaForm(forms.ModelForm):

    class Meta:
        model = Anagrafica
        fields = ('nome','cognome')