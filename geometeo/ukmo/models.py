#from django.db import models
from django.contrib.gis.db import models

class Ray(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    datetime = models.DateTimeField()
    error = models.FloatField()

    #especifico de geodjango
    geopoint = models.PointField(srid=4326)
    objects = models.GeoManager()

    # Returns the string representation of the model.
    def __unicode__(self):
        return '%s %s' % (self.geopoint.x, self.geopoint.y)

