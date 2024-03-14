from django import forms

from .models import Articoli

class ArticoliForm(forms.ModelForm):
    class Meta:
        model = Articoli
        fields = ['codice', 'descrizione']
        # fields = ['ditta', 'codice', 'descrizione']