from django.db import models

class Anagrafica(models.Model):
    nome = models.CharField(max_length=30, blank=True, null=True)
    cognome = models.CharField(max_length=30, blank=True, null=True)

    def __str__(self):
        return str(self.nome) + " " + str(self.cognome)

    class Meta:
        verbose_name = "Anagrafica"
        verbose_name_plural = "Anagrafiche"
