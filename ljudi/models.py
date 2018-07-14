from django.db import models


class Zaposleni(models.Model):
    AKTIVAN = "A"
    NEAKTIVAN = "N"
    STATUS_CHOICES = (
        (AKTIVAN, "Aktivan"),
        (NEAKTIVAN, "Neaktivan")
    )
    JMBG = models.CharField(max_length=25, null=True, blank=True)
    ime_prezime = models.CharField(max_length=50)
    adresa = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES)
    nadredjeni = models.ForeignKey(
        'self',
        on_delete=models.CASCADE, blank=True, null=True)
    projekti = models.ManyToManyField('Projekat', through='Projekat_Zaposleni')

    def __str__(self):
        return self.ime_prezime

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
    naziv = models.CharField(max_length=255)
    zaposleni = models.ManyToManyField('Zaposleni', through='Projekat_Zaposleni')


    def __str__(self):
        return self.naziv

    class Meta:
        verbose_name = "Projekat"
        verbose_name_plural = "Projekti"


class Projekat_Zaposleni(models.Model):
    zaposleni = models.ForeignKey('Zaposleni', related_name='zaposleni')
    projekat = models.ForeignKey('Projekat', related_name='projekti')
    od_datuma = models.DateField()
    do_datuma = models.DateField()


class Sredstvo_za_rad(models.Model):
    naziv = models.CharField(max_length=255)


class Dani_odsustva(models.Model):
    Od_dana = models.DateField()
    Do_data = models.DateField()
    # Broj_dana = models.IntegerField()   kako ovo da bude kalkulativna kolona
