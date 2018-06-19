from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from django import forms
from .models import Recepient, Envelop
from .forms import AddRecepientForm, RecepientDetailForm, AddEnvelopeModelForm
from itertools import chain
from mailmerge import MailMerge



def env_generate (title, address, postcode, recep_id):
    template = r'C:\Users\d051a\Desktop\project\django19\webprint\_WEBPRINT\media\templ.docx'
    document = MailMerge(template)
    #print('Fields:', document.get_merge_fields())
    document.merge(
        TITLE = title,
        ADDRESS = address,
        POSTCODE = postcode, )
    document.write(r'C:\Users\d051a\Desktop\project\django19\webprint\_WEBPRINT\media\00{}.docx'.format(recep_id))


def envelops (request):
    envelops_list = Envelop.objects.all()
    return render(request, 'envelops.html', {'envelops_list': envelops_list})

def recepients (request):
    recepients_list = Recepient.objects.order_by("-pk")
    envelop_list = Envelop.objects.all()
    print (recepients_list)
    return render(request, 'recepients.html', {'recepients_list': recepients_list,
                                                'envelop_list': envelop_list})


def recepient_add(request):
    if request.method == 'POST':
        form = AddRecepientForm(request.POST)
        recepient_count = Recepient.objects.all().count()
        if form.is_valid():
            cld = form.cleaned_data
            recepient = Recepient()
            recepient.title = cld['title']
            recepient.address = cld['address']
            recepient.postcode = cld['postcode']
            env_generate (recepient.title, recepient.address, recepient.postcode, recepient_count+1)
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
            env_generate (recepient.title, recepient.address, recepient.postcode, rec_id)
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


def envelop_add(request):
    if request.method == 'POST':
        form = AddEnvelopeModelForm(request.POST, request.FILES)
        if form.is_valid():
            cld = form.cleaned_data
            envelop = Envelop()
            envelop.env_title = cld['env_title']
            envelop.envelop_format = cld['envelop_format']
            envelop.envelop_template = cld['envelop_template']
            envelop.save()
            return HttpResponseRedirect('/')
    else:
        form = AddEnvelopeModelForm()
    return render(request, 'envelop_add.html', {'form': form})
