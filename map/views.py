from django.http import HttpResponse
from django.template import loader
from django.urls import reverse


def index(request):
    template = loader.get_template("map/map.html")
    context = {
        "title": "Map",
        "layer_urls": [
            reverse("stay-list"),
            reverse("sidetrip-list"),
        ]
    }
    return HttpResponse(template.render(context=context, request=request))
