from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from cards.views import PlayerView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cah.views.home', name='home'),
    # url(r'^cah/', include('cah.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', PlayerView.as_view(), name="player-view",),
    url(r'^admin/', include(admin.site.urls)),
)
