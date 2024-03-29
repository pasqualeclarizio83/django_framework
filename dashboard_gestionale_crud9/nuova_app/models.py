from django.db import models

# La relazione 1 a 1 è rappresentata 
# tra Dipartimento e Facolta, poiché ogni 
# facoltà è associata a un singolo dipartimento.

class Dipartimento(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

# La relazione 1 a molti è rappresentata 
# tra Facolta e Corso, in quanto una 
# facoltà può offrire molti corsi.

class Facolta(models.Model):
    nome = models.CharField(max_length=100)
    dipartimento = models.ForeignKey(Dipartimento, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Corso(models.Model):
    nome = models.CharField(max_length=100)
    facolta = models.ForeignKey(Facolta, on_delete=models.CASCADE)

    def __str__(self):
        return self.nome

class Professore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    facolta = models.ForeignKey(Facolta, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.facolta.nome})"

# La relazione molti a molti è 
# rappresentata tra Studente e Insegnamento 
# attraverso il modello Iscrizione, 
# poiché uno studente può iscriversi a molti 
# insegnamenti e un insegnamento può avere 
# molti studenti iscritti.

class Studente(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    corso_di_laurea = models.ForeignKey(Corso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} {self.cognome} ({self.corso_di_laurea.nome})"

class Insegnamento(models.Model):
    nome = models.CharField(max_length=100)
    professore = models.ForeignKey(Professore, on_delete=models.CASCADE)
    corso = models.ForeignKey(Corso, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome} {self.professore} ({self.corso.nome})"

class Iscrizione(models.Model):
    studente = models.ForeignKey(Studente, on_delete=models.CASCADE)
    insegnamento = models.ForeignKey(Insegnamento, on_delete=models.CASCADE)