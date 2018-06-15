from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import Recepient, Envelop
from django import forms
from itertools import chain

#from mailmerge import mailmerge



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
    env_title = models.CharField('Название конверта', max_length=30)
    envelop_format = models.ForeignKey('Формат конверта', Envelop_format)
    envelop_template = models.FileField('Шаблон конверта',
                                        upload_to='/home/d051a/Desktop/PythonProjects/_webprint/_WEBPRINT/upload/')'''


def envelops (request):
    envelops_list = Envelop.objects.all()
    return render(request, 'envelops.html', {'envelops_list': envelops_list})

def recepients (request):
    recepients_list = Recepient.objects.order_by("-pk")
    print (recepients_list)
    return render(request, 'recepients.html', {'recepients_list': recepients_list})

def recepient_add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = AddRecepientForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            recepient = Recepient()
            recepient.title = cld['title']
            recepient.address = cld['address']
            recepient.postcode = cld['postcode']
            recepient.save()
            return HttpResponseRedirect('/')
    else:
        form = AddRecepientForm()
    return render(request, 'recepient_add.html', {'form': form})

def recepient_detail(request, rec_id):
    recepient_detail = Recepient.objects.get(pk=rec_id)
    if request.method == 'POST':
        form = RecepientDetailForm(request.POST)
        if form.is_valid():
            cld = form.cleaned_data
            recepient = Recepient.objects.get(pk=rec_id)
            recepient.title = cld['title']
            recepient.address = cld['address']
            recepient.postcode = cld['postcode']
            recepient.save()
            return HttpResponseRedirect('/')
    else:
        form = RecepientDetailForm({'title': recepient_detail.title,
                                    'address': recepient_detail.address,
                                    'postcode': recepient_detail.postcode})

    return render(request, 'recepient_detail.html', {'form': form,
                                                     'title': recepient_detail.title,
                                                     'address': recepient_detail.address,
                                                     'postcode': recepient_detail.postcode
                                                     })


'''def test (request):
    template = r'D:\_YANDEXDRIVE\_ADMIN\_PYTHON\_wordtempl\templ.docx'

    document = mailmerge(template)
    print(document.get_merge_fields())

    document.merge(
        Name='Gold',
        LASTNAME='Springfield', )

    document.write(r'D:\_YANDEXDRIVE\_ADMIN\_PYTHON\_wordtempl\test-output.docx')
    return HttpResponse ("hello!")'''
