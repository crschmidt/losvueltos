from django.db import models

#fabio@fa-casa:~/losvueltos/geometeo$ python manage.py ogrinspect --mapping --multi shapes/europe_administrative.shp europe_administrative
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class europe_administrative(models.Model):
    name = models.CharField(max_length=142)
    admin_leve = models.CharField(max_length=20)
    geom = models.MultiLineStringField()
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for europe_administrative model
europe_administrative_mapping = {
    'name' : 'NAME',
    'admin_leve' : 'ADMIN_LEVE',
    'geom' : 'MULTILINESTRING',
}

#fabio@fa-casa:~/losvueltos/geometeo$ python manage.py ogrinspect --mapping --multi shapes/europe_coastline.shp europe_coastline
# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class europe_coastline(models.Model):
    natural = models.CharField(max_length=9)
    name = models.CharField(max_length=45)
    geom = models.MultiLineStringField()
    objects = models.GeoManager()

# Auto-generated `LayerMapping` dictionary for europe_coastline model
europe_coastline_mapping = {
    'natural' : 'NATURAL',
    'name' : 'NAME',
    'geom' : 'MULTILINESTRING',
}

