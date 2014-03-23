from django.conf.urls import patterns, include, url
from nom020.views import hello, current_datetime, hours_ahead, calculation
from django.contrib import admin
admin.autodiscover()
from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nom020.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
    url( r'^hello/$', hello ),
    url( r'^time/$', current_datetime ),
    url( r'^time/plus/(\d{1,2})/$',hours_ahead ),
    #url( r'^nom/$', calculation ),
    url(r'^nom/', include('nom.urls')),
)

urlpatterns += staticfiles_urlpatterns()