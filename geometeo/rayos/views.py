# Create your views here.

# django imports
from django.conf import settings
from django.shortcuts import render_to_response


# Django imports to contruct welcome message
from django.template import Template, Context
from django.http import HttpResponse


def pinta_rayos(request):
    return render_to_response('rayos.html')

