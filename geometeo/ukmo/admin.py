from django.contrib.gis import admin
from geometeo.ukmo.models import Ray

admin.site.register(Ray, admin.OSMGeoAdmin)
