#from django.db import models
from django.contrib.gis.db import models

# Create your models here.

class rayos_ukmo(models.Model):
	lon = models.FloatField()
	lat = models.FloatField()
	fecha = models.DateTimeField()
	error = models.FloatField()

	#especifico de geodjango
	geopunto = models.PointField(srid=4326)
	objects = models.GeoManager()

# Returns the string representation of the model.
def __unicode__(self):
	return '%s %s %s' % (self.name, self.geometry.x, self.geometry.y)

