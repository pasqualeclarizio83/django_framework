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