# Import django modules
from django.conf.urls.defaults import *


urlpatterns = patterns('geometeo.rayos.views',
    url(r'^$', 'index', name='rayos-index'),
)

