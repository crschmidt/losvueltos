from django.contrib.gis import admin
from models import rayos_ukmo

#admin.site.register(rayos_ukmo, admin.GeoModelAdmin)
admin.site.register(rayos_ukmo, admin.OSMGeoAdmin)
