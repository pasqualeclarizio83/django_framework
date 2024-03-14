from django.db import models

class Deposito(models.Model):
    loc_deposito = models.CharField(max_length=2, blank=True, null=True)
    descrizione = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return str(self.loc_deposito) # str(self.pk)

    class Meta:
        verbose_name = "Deposito"
        verbose_name_plural = "Depositi"

class Articoli(models.Model):
    ditta = models.DecimalField(max_digits=5, decimal_places=0, default=1)
    codice = models.CharField(max_length=25, blank=True, null=True)
    descrizione = models.CharField(max_length=72, blank=True, null=True)
    
    def __str__(self):
        return self.descrizione

    class Meta:
        verbose_name = "Articolo"
        verbose_name_plural = "Articoli"