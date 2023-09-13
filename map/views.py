from itertools import chain

from django.core.serializers import serialize
from django.http import HttpResponse
from django.template import loader

from loader.models import SideTrip, Stay


# Create your views here.
def index(request):
    template = loader.get_template("map/map.html")
    return HttpResponse(template.render(context=dict(), request=request))


def data(request):
    stays = Stay.objects.all()
    side_trips = SideTrip.objects.all()

    return HttpResponse(
        serialize("geojsoncss", list(chain(stays, side_trips)), fields=["id", "name"], geometry_field="location"),
        content_type='application/json'
    )
