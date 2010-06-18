# Create your views here.

# django imports
from django.conf import settings
from django.shortcuts import render_to_response


# Django imports to contruct welcome message
from django.template import Template, Context
from django.http import HttpResponse

# vectorformats
from vectorformats.Formats import Django, GeoJSON
from rayos.models import rayos_ukmo


def pinta_rayos(request):
    json = calcula_json()
    return render_to_response('rayos-json.html')

def calcula_json():
    qs = rayos_ukmo.objects.filter(error__gt=5)
    djf = Django.Django(geodjango="geopoint", properties=['error', 'lat','lon'])
    geoj = GeoJSON.GeoJSON()
    string = geoj.encode(djf.decode(qs))
    return string

