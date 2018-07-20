from django import forms
from .models import Zaposleni, Dani_odsustva, Sredstvo_za_rad, Template_resenja


class ZaposleniForm(forms.ModelForm):
    class Meta:
        model = Zaposleni
        fields = ["JMBG", "ime_prezime", "adresa", "status", "nadredjeni"]


class OdsustvaForm(forms.ModelForm):
    class Meta:
        model = Dani_odsustva
        fields = ["zaposleni", "tip", "Od_dana", "Do_data"]


class TemplateResenjaForm(forms.ModelForm):
    class Meta:
        model = Template_resenja
        fields = ('naziv', 'opis', 'document', 'tip')


# class SredstvaZaRadCreateForm(forms.ModelForm):
#     deo_sredstva = forms.ModelMultipleChoiceField(queryset=Sredstvo_za_rad.objects.all(), required=False)
#
#     class Meta:
#         model = Sredstvo_za_rad
#         fields = ['naziv', 'vrednost', 'datum_kupovine', 'zaposleni', 'deo_sredstva']
#
#     # def __init__(self, *args, **kwargs):
#     #     # Only in case we build the form from an instance
#     #     # (otherwise, 'toppings' list should be empty)
#     #     if kwargs.get('instance'):
#     #         # We get the 'initial' keyword argument or initialize it
#     #         # as a dict if it didn't exist.
#     #         initial = kwargs.setdefault('initial', {})
#     #         # The widget for a ModelMultipleChoiceField expects
#     #         # a list of primary key for the selected data.
#     #         initial['deo_sredstva'] = [t.pk for t in kwargs['instance'].deo_sredstva_set.all()]
#     #
#     #     forms.ModelForm.__init__(self, *args, **kwargs)
#     #
#     #     # Overriding save allows us to process the value of 'toppings' field
#
#     # def save(self, commit=True):
#     #     # Get the unsave Pizza instance
#     #     instance = forms.ModelForm.save(self, False)
#     #
#     #     # Prepare a 'save_m2m' method for the form,
#     #     old_save_m2m = self.save_m2m
#     #
#     #     def save_m2m():
#     #         old_save_m2m()
#     #         # This is where we actually link the pizza with toppings
#     #         instance.deo_sredstva_set.clear()
#     #         for topping in self.cleaned_data['deo_sredstva']:
#     #             instance.deo_sredstva_set.add(topping)
#     #
#     #     self.save_m2m = save_m2m
#     #
#     #     # Do we need to save all changes now?
#     #     if commit:
#     #         instance.save()
#     #         self.save_m2m()
#     #
#     #     return instance
