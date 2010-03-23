from django.views.generic.simple import direct_to_template
from geometeo.ukmo.models import Ray
from django.http import HttpResponse

def render_map(request, object_list):
    """
    Feeds data out to our map template.
    """
    context = {}

    # Add it to the context we'll pass out to the template
    context['object_list'] = object_list

    return direct_to_template(request, 'ukmo/rays/rays.html', context)

def index(request):
    rays_list = Ray.objects.all().order_by('datetime')[:10]
    
    return render_map(request, rays_list)
