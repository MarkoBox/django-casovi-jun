from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.shortcuts import render
from .models import *
from .forms import ZaposleniForm
from django_tables2 import RequestConfig
from .table import ZaposleniTable
from django.http import HttpResponse

import csv


class HomePageView(TemplateView):
    template_name = 'home.html'


class SredstvaZaRadListView(ListView):
    model = Sredstvo_za_rad
    template_name = 'sredstva_za_rad.html'


class SredstvaZaRadDetailView(DetailView):
    # odakle ovo ovde
    model = Sredstvo_za_rad
    template_name = 'sredstvo_za_rad.html'


# ovo ne radi dobro
class SredstvaZaRadCreateView(CreateView):
    model = Sredstvo_za_rad
    template_name = 'sredstva_za_rad_create_form.html'
    fields = ['naziv', 'vrednost', 'datum_kupovine', 'zaposleni', 'deo_sredstva']


# ne radi
class SredstvaZaRadUpdateView(UpdateView):
    model = Sredstvo_za_rad
    fields = ['naziv', 'vrednost', 'datum_kupovine', 'zaposleni', 'deo_sredstva']
    template_name = 'Sredstvo_za_rad_update_form.html'


# kako da vratim related polja
def export_sredstva_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="sredstva.csv"'

    writer = csv.writer(response)
    writer.writerow([field.name for field in Sredstvo_za_rad._meta.get_fields()])

    sredstva = Sredstvo_za_rad.objects.all().values_list(*[field.name for field in Sredstvo_za_rad._meta.get_fields()])
    for sredstvo in sredstva:
        writer.writerow(sredstvo)

    return response


class ProjektiListVIew(ListView):
    model = Projekat
    template_name = 'projekti.html'


def zaposleni_table_view(request):
    table = ZaposleniTable(Zaposleni.objects.all())
    RequestConfig(request).configure(table)
    return render(request, 'zaposleni.html', {'table': table})


class OdsustvaListView(ListView):
    model = Dani_odsustva
    template_name = 'odsustva.html'


def zaposleni_new(request):
    if request.method == "POST":

        form = ZaposleniForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ZaposleniForm()
    return render(request, 'dodaj_zaposlenog.html', {'pera': form})
