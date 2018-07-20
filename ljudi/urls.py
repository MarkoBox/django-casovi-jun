from django.conf.urls import url
from . import views
from django.urls import path

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('sredstva_za_rad/', views.SredstvaZaRadListView.as_view(), name='sredstva_za_rad'),
    path('sredstva_za_rad/<int:pk>/', views.SredstvaZaRadDetailView.as_view(), name='sredstvo_za_rad'),
    path('sredstva_za_rad/dodaj_sredstvo', views.SredstvaZaRadCreateView.as_view(), name='dodaj_sredstvo'),
    path('sredstva_za_rad/update_sredstvo/<int:pk>/', views.SredstvaZaRadUpdateView.as_view(), name='update_sredstvo'),
    path('sredstva_za_rad/export/csv', views.export_sredstva_csv, name='export_sredstva_csv'),
    path('projekti/', views.ProjektiListVIew.as_view(), name='projekti'),
    path('zaposleni/', views.zaposleni_table_view, name='zaposleni'),
    path('zaposleni/dodaj_zaposlenog', views.zaposleni_new, name='dodaj_zaposlenog'),
    path('odsustva/', views.OdsustvaListView.as_view(), name='odsustva'),
    # path('odsustva/dodaj', views.odsustva_new, name='odsustva_dodaj'),
    path('odsustva/dodaj',
         views.OdsustvaCreateView.as_view(), name='odsustva_dodaj'),
    path('upload_template', views.upload_template, name='template_resenja'),
    # url(r'^$', views.zaposleni_new, name='dodaj_zaposlenog'),
]
