from django.conf.urls.defaults import *
from django.contrib.gis import admin
import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^ukmo/rays/$', 'geometeo.ukmo.views.index'),
#    (r'^rayos/(?P<rayo_id>\d+)/$', 'geometeo.rayos.views.detail'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    # Set
    mediaURL = settings.MEDIA_URL[1:]
    # Extend
    urlpatterns += patterns('',
        (r'^%s(?P<path>.*)$' % mediaURL, 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
    )

