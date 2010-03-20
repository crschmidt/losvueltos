# Create your views here.
import logging

from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.template.loader import render_to_string
from geometeo.rayos.models import rayos_ukmo

#def index(request):
#    return render_to_response('rayos/index.html', {
#    })

def index(request):
    rayos = rayos_ukmo.objects.all()
    #for rayo in rayos:
	#print rayo.geopunto.y
        #print rayo.geopunto.x
    #logging.debug("pedimos rayos")
    return render_to_response('rayos/index.html', {
        'rayos': rayos,
        'content': render_to_string('rayos/rayos.html', {'rayos': rayos}),
    })


#def index(request):
#    return HttpResponse('Hello')

