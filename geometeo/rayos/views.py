# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render_to_response

from django.template.loader import render_to_string
from geometeo.rayos.models import rayos_ukmo

def index(request):
    rayos = rayos_ukmo.objects.all()

    return render_to_response('rayos/index.html', {
        'rayos': rayos,
        'content': render_to_string('rayos/rayos.html', {'rayos': rayos}),
    })

#def index(request):
#    return HttpResponse('Hello')

