from django.conf.urls import patterns, include, url
from nom020.views import hello, current_datetime, hours_ahead, calculation
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'nom020.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url( r'^hello/$', hello ),
    url( r'^time/$', current_datetime ),
    url( r'^time/plus/(\d{1,2})/$',hours_ahead ),
    #url( r'^nom/$', calculation ),
    url(r'^nom/', include('nom.urls')),
    url(r'^analytics/', include('analytics.urls')),
)