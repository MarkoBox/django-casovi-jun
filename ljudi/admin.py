from django.contrib import admin

from .models import Zaposleni, Projekat, Projekat_Zaposleni, Sredstvo_za_rad, Deo_sredstva, Importovan_dokument,\
    Tip_odsustva, Dani_odsustva, Template_resenja

admin.site.register(Zaposleni)
admin.site.register(Projekat)
admin.site.register(Projekat_Zaposleni)
admin.site.register(Sredstvo_za_rad)
admin.site.register(Deo_sredstva)
admin.site.register(Importovan_dokument)
admin.site.register(Tip_odsustva)
admin.site.register(Dani_odsustva)
admin.site.register(Template_resenja)
