from django.db import models


class Zaposleni(models.Model):
    JMBG = models.CharField(max_length=25, null=True, blank=True)
    Ime_prezime = models.CharField(max_length=50)
    Adresa = models.CharField(max_length=200, null=True, blank=True)
    Nadredjeni = models.ForeignKey(
        'self',
        on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.Ime_prezime

    class Meta:
        verbose_name = "Zaposleni"
        verbose_name_plural = "Zaposleni"

    # MANAGERS
    # TODO Implement managers

    # SAVE METHOD
    # TODO IMPLEMENT SAVE METHOD

    # ABSOLUTE URL METHOD
    # TODO IMPLEMENT URL METHODS

    # OTHER METHODS


class Projekat(models.Model):
    Naziv = models.CharField(max_length=255)


    def __str__(self):
        return self.Naziv

    class Meta:
        verbose_name = "Projekat"
        verbose_name_plural = "Projekti"




class Dani_odsustva(models.Model):
    Od_dana = models.DateField()
    Do_data = models.DateField()
    Broj_dana = models.IntegerField()  # kako ovo
