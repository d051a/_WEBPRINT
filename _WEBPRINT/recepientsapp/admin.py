from django.contrib import admin
from recepientsapp.models import Recepient_person, Address, Recepient_legal

admin.site.register(Recepient_person)
admin.site.register(Address)
admin.site.register(Recepient_legal)
