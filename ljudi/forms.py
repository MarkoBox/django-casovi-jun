from django.forms import ModelForm
from .models import Zaposleni, Dani_odsustva


class ZaposleniForm(ModelForm):
    class Meta:
        model = Zaposleni
        fields = ["JMBG", "ime_prezime", "adresa", "status", "nadredjeni"]


class OdsustvaForm(ModelForm):
    class Meta:
        model = Dani_odsustva
        fields = ["zaposleni", "tip", "Od_dana", "Do_data"]