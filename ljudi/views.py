from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView
from django.shortcuts import render
from .forms import ZaposleniForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class SredstvaZaRadListView(ListView):
    template_name = 'sredstva_za_rad.html'

class SredstvaZaRadDetailView(DetailView):
    pass

class Projekti(ListView):
    template_name = 'projekti.html'


class Zaposleni(ListView):
    template_name = 'zaposleni.html'


class Odsustva(ListView):
    template_name = 'odsustva.html'


def zaposleni_new(request):
    if request.method == "POST":

        form = ZaposleniForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ZaposleniForm()
    return render(request, 'dodaj_zaposlenog.html', {'pera': form})
