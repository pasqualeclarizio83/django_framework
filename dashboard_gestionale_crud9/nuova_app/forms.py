from django import forms

from .models import Facolta

class FacoltaForm(forms.ModelForm):
    class Meta:
        model = Facolta
        fields = ['nome', 'dipartimento']