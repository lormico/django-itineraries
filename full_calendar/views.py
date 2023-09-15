import json

from django.http import HttpResponse
from django.template import loader

from full_calendar.services import get_events


def index(request):
    template = loader.get_template("fullcalendar/index.html")
    events = get_events()
    return HttpResponse(template.render(context={"title": "Calendar", "events": json.dumps(events)}, request=request))
