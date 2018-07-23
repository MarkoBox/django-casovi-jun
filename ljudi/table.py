import django_tables2 as tables
from .models import Zaposleni


class ZaposleniTable(tables.Table):
    class Meta:
        model = Zaposleni
        template_name = 'django_tables2/bootstrap.html'

