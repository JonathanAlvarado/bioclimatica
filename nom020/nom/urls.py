from django.conf.urls import patterns, url, include
from nom import views
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
)

urlpatterns += staticfiles_urlpatterns()