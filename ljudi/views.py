from django.views.generic import TemplateView
from django.shortcuts import render
from .forms import ZaposleniForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class SredstvaZaRad(TemplateView):
    template_name = 'sredstva_za_rad.html'


class Projekti(TemplateView):
    template_name = 'projekti.html'


class Zaposleni(TemplateView):
    template_name = 'zaposleni.html'


class Odsustva(TemplateView):
    template_name = 'odsustva.html'


def zaposleni_new(request):
    if request.method == "POST":

        form = ZaposleniForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ZaposleniForm()
    return render(request, 'dodaj_zaposlenog.html', {'pera': form})
