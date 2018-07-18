from django.forms import ModelForm
from .models import Zaposleni


class ZaposleniForm(ModelForm):

    class Meta:
        model = Zaposleni
        fields = ["JMBG", "ime_prezime", "adresa", "status", "nadredjeni"]


