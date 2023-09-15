from django.http import HttpResponse
from django.template import loader


# Create your views here.
def index(request):
    template = loader.get_template("map/map.html")
    return HttpResponse(template.render(context={"title": "Map"}, request=request))
