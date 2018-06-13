from django.conf.urls import url
from . import views

#app_name = 'recepientsapp'

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.recepients, name='recepients'),
    url(r'recepient/(\d+)/$', views.recepient_detail, name='recepient_detail'),
    url(r'recepient_add/$', views.recepient_add, name='recepient_add'),
    url(r'envelops/$', views.envelops, name='envelops'),
    #url(r'envelops_add/$', views.envelop_add, name='envelop_add'),
    #url(r'envelop/(\d+)/$', views.envelop_detail, name='envelop_detail'),
]
