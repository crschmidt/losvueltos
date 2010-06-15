from django.contrib.gis import admin
from models import europe_administrative

#admin.site.register(rayos_ukmo, admin.GeoModelAdmin)
admin.site.register(europe_administrative, admin.OSMGeoAdmin)
