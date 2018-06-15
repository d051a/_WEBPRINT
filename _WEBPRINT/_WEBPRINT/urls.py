from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse


urlpatterns = [
    # Examples:
    # url(r'^$', '_WEBPRINT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('recepientsapp.urls', namespace='recepientsapp')),

]
