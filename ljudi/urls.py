from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('sredstva_za_rad/', views.SredstvaZaRad.as_view(), name='sredstva_za_rad'),
    path('projekti/', views.Projekti.as_view(), name='projekti'),
    path('zaposleni/', views.Zaposleni.as_view(), name='zaposleni'),
    path('odsustva/', views.Odsustva.as_view(), name='odsustva'),
    #url(r'^$', views.zaposleni_new, name='dodaj_zaposlenog'),
]