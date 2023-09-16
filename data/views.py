from itertools import chain

from django.core.serializers import serialize
from django.http import HttpResponse
from django.template import loader
from rest_framework import viewsets

from data.models import Leg, SideTrip, Stay, Website
from data.serializers import LegSerializer, SideTripSerializer, StaySerializer, WebsiteSerializer


class LegViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Leg.objects.all()
    serializer_class = LegSerializer
    # permission_classes = [permissions.IsAuthenticated]


class SideTripViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = SideTrip.objects.all()
    serializer_class = SideTripSerializer
    # permission_classes = [permissions.IsAuthenticated]


class StayViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Stay.objects.all()
    serializer_class = StaySerializer
    # permission_classes = [permissions.IsAuthenticated]


class WebsiteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Website.objects.all()
    serializer_class = WebsiteSerializer
    # permission_classes = [permissions.IsAuthenticated]


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
