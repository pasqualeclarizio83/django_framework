from django.db import models

class Deposito(models.Model):
    loc_deposito = models.CharField(max_length=2, blank=True, null=True)
    descrizione = models.CharField(max_length=120, blank=True, null=True)

    def __str__(self):
        return str(self.loc_deposito) # str(self.pk)

    class Meta:
        verbose_name = "Deposito"
        verbose_name_plural = "Depositi"
