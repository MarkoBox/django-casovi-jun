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

    def __str__(self):
        return f"Zaposleni {self.zaposleni} je na projektu {self.projekat} od {self.od_datuma} do {self.do_datuma}"


class Sredstvo_za_rad(models.Model):
    naziv = models.CharField(max_length=255)
    vrednost = models.DecimalField(max_digits=30, decimal_places=2)
    datum_kupovine = models.DateField()
    zaposleni = models.ForeignKey('Zaposleni', related_name='zaposleni')
    deo_sredstva = models.ManyToManyField('self', through="Deo_sredstva", symmetrical=False, related_name='je_deo')

    def __str__(self):
        return self.naziv


class Deo_sredstva(models.Model):
    iz_sredstva = models.ForeignKey(Sredstvo_za_rad, related_name='iz_sredstva')
    u_sredstvo = models.ForeignKey(Sredstvo_za_rad, related_name='u_sredstvo')
    procenat_promene = models.DecimalField(max_digits=1, decimal_places=2)  # ovo bi trebalo da je procenat
    vrednost = models.DecimalField(max_digits=30, decimal_places=2)
    datum_promene = models.DateField()

    def __str__(self):
        return self.datum_promene


class Importovan_dokument(models.Model):
    naziv = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    ekstenzija = models.CharField(max_length=10)

    def __str__(self):
        return self.naziv


class Tip_odsustva(models.Model):
    naziv = models.CharField(max_length=255)
    Opis = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.naziv


class Dani_odsustva(models.Model):
    Od_dana = models.DateField()
    Do_data = models.DateField()
    # Broj_dana = models.IntegerField()   kako ovo da bude kalkulativna kolona
    dokument = models.ForeignKey('Importovan_dokument', related_name='dokument')
    zaposleni = models.ForeignKey('Zaposleni', related_name='zaposleni')
    tip = models.ForeignKey('Tip_odsustva', related_name='tip_odsustva')


class Template_resenja(models.Model):
    naziv = models.CharField(max_length=255)
    path = models.CharField(max_length=255)
    tip = models.ForeignKey('Tip_odsustva', related_name='tip_odsustva')

    def __str__(self):
        return self.naziv
