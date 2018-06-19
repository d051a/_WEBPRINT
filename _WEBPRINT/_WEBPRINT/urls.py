from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', '_WEBPRINT.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('recepientsapp.urls', namespace='recepientsapp')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
