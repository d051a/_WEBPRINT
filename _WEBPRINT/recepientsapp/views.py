from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import RequestContext, loader
from .models import Recepient_person
from django import forms

'''
def index(request):
    output = "Hello!"

    template = loader.get_template('recepients.html')
    recepients_list = Recepient_person.objects.all()
    context = RequestContext(request, {'recepients_list': recepients_list})
    return HttpResponse(template.render(context))

'''
class AddRecepientForm(forms.Form):
    name = forms.CharField(label = 'Имя', max_length = 30)
    lastname = forms.CharField(label = 'Фамилия', max_length = 30)
    patronymic = forms.CharField(label = 'Отчество', max_length = 30)
    #pub_date = forms.DateField(label = 'date published')
    address = forms.CharField(label = 'Адрес', max_length = 100)
    index = forms.CharField(label = 'Индекс', max_length = 6)

def recepient_add(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = AddRecepientForm(request.POST)
        # check whether it's valid:
        print (request)
        if form.is_valid():
            print (request)
            cld = form.cleaned_data
            recepient_person = Recepient_person()
            recepient_person.Name = cld['name']
            recepient_person.LastName = cld['lastname']
            recepient_person.Patronymic = cld['patronymic']
            recepient_person.address = cld['address']
            recepient_person.index = cld['index']
            recepient_person.save()
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/recepients/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = AddRecepientForm()
        print (request)

    return render(request, 'recepient_add.html', {'form': form})



def recepients (request):
    recepients_list = Recepient_person.objects.all()
    return render(request, 'recepients.html', {'recepients_list': recepients_list})

def recepient_detail (request, rec_id):
    recepient_detail = Recepient_person.objects.get(pk=rec_id)
    return render(request, 'recepient_detail.html', {'recepient_detail': recepient_detail})
