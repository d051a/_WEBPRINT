from django.shortcuts import render
from .models import Person

def people(request):
    return render(request, 'people.html', {'people': Person.objects.all()})
