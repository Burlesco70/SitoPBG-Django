from django.db import models

class Corso(models.Model):
    # Struttura/Attributi
    nome = models.CharField(max_length=100, help_text="Nome del corso")
    insegnante = models.CharField(max_length=100, help_text="Nome insegnante/tutore")
    livello = models.CharField(max_length=100, help_text="Livello")
    descrizione = models.CharField(max_length=255, help_text="Descrizione corso")
    stato_corso = models.CharField(max_length=30, help_text="Stato corso")
    link_materiale = models.CharField(max_length=255, help_text="Link materiale")

    # Relazione 1:n; ordinamento serate per data
    # serate = db.relationship(
    #     "Serata", order_by="asc(Serata.data)", backref="corso", lazy="subquery"
    # )

    # Relazione n:n
    # tags = db.relationship(
    #     "Tag", secondary=tags, lazy="subquery", backref=db.backref("corso", lazy=True),
    # )

    def __str__(self):
        return f"Corso {self.nome}"


class Serata(models.Model):
    nome = models.CharField(max_length=100, help_text="Nome serata")
    descrizione = models.CharField(max_length=255, help_text="Descrizione serata")
    data = models.DateField()
    link_partecipazione = models.CharField(max_length=255, help_text="Link partecipazione")
    link_registrazione = models.CharField(max_length=255, help_text="Link registrazione")
    corso = models.ForeignKey(to=Corso, on_delete=models.PROTECT)

