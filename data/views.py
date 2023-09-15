from itertools import chain

from django.core.serializers import serialize
from django.http import HttpResponse
from django.template import loader

from data.models import SideTrip, Stay


def index(request):
    stays = Stay.objects.all()
    side_trips = SideTrip.objects.all()

    return HttpResponse(
        serialize("geojsoncss", list(chain(stays, side_trips)), fields=["id", "name"], geometry_field="location"),
        content_type='application/json'
    )


def report(request):
    template = loader.get_template("data/reports.html")
    return HttpResponse(template.render(context={"title": "Reports"}, request=request))
