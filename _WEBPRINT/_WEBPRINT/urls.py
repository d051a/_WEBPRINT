from django.conf.urls import include, url
from django.contrib import admin
from tutorial.views import people
from django.http import HttpResponse

def index(request):
    return HttpResponse ('MAIN PAGE')

urlpatterns = [
    # Examples:
    # url(r'^$', '_WEBPRINT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^recepients/', include('recepientsapp.urls')),
]
