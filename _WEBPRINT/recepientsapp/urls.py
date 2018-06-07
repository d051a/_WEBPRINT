from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.recepients, name='recepients'),
    url(r'recepient/(\d+)/$', views.recepient_detail, name='recepient_detail'),
    url(r'recepient_add/$', views.recepient_add, name='recepient_add'),
]
