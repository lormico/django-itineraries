import json

from django.http import HttpResponse
from django.template import loader

from full_calendar.services import get_events, get_initial_date


def index(request):
    template = loader.get_template("fullcalendar/index.html")
    events = get_events()
    initial_date = get_initial_date(events)
    context = {
        "title": "Calendar",
        "events": json.dumps(events),
        "initial_date": initial_date,
        "time_zone": "Asia/Tokyo",
    }
    return HttpResponse(template.render(context=context, request=request))
