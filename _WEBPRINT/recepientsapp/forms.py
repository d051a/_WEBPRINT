from django import forms
from django.db import models
from .models import Envelop
from django.forms import ModelForm

class AddRecepientForm(forms.Form):
    title = forms.CharField(label = 'Имя', max_length = 30)
    #pub_date = forms.DateField(label = 'date published')
    address = forms.CharField(label = 'Адрес', max_length = 100)
    postcode = forms.CharField(label = 'Индекс', max_length = 6)

class RecepientDetailForm(forms.Form):
    title = forms.CharField(label = 'Имя', max_length = 30)
    #pub_date = forms.DateField(label = 'date published')
    address = forms.CharField(label = 'Адрес', max_length = 100)
    postcode = forms.CharField(label = 'Индекс', max_length = 6)

'''class AddEnvelopeForm(forms.Form):
    env_title = forms.CharField()
    envelop_format = forms.MenuModelChoiceField(queryset=Menu.objects.all())
    envelop_template = forms.FileField()'''

class AddEnvelopeModelForm(ModelForm):
    class Meta:
        model = Envelop
        fields = ['env_title', 'envelop_format', 'envelop_template']
