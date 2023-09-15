from datetime import timedelta
from typing import Dict, List

from django.contrib.staticfiles import finders
from skyfield import api, almanac

from loader.admin.models import try_make_naive
from loader.models import Stay

ts = api.load.timescale()
ephemerids_file = finders.find("de421.bsp")
eph = api.load(ephemerids_file)


def get_events() -> List[Dict[str, str]]:
    """
    Returns a list of events to load in the calendar.

    :returns: a list of events
    """
    stays = Stay.objects.all()
    stay_events = [
        {
            "title": stay.name,
            "start": stay.checkin.isoformat(),
            "end": stay.checkout.isoformat(),
            "display": "background"
        } for stay in stays
    ]

    return stay_events + get_night_events(stays)


def get_night_events(stays) -> List[Dict[str, str]]:
    """
    Returns a list of events lasting the whole night (sunset to sunrise)
    for each of the stays' nights.

    Night events are background events with custom class name ``event-night``.

    :param stays: an iterable of Stays
    :returns: a list of events
    """
    night_events = list()
    for stay in stays:
        lon, lat = stay.location
        stay_nights = (
                try_make_naive(stay.checkout, lat, lon).date() -
                try_make_naive(stay.checkin, lat, lon).date()).days
        stay_days = [stay.checkin + timedelta(days=day) for day in range(stay_nights)]
        stay_location = api.wgs84.latlon(lat, lon)
        for stay_day in stay_days:
            t0 = ts.from_datetime(stay_day)
            t1 = ts.from_datetime(stay_day + timedelta(days=1))
            (sunset, sunrise), _ = almanac.find_discrete(t0, t1, almanac.sunrise_sunset(eph, stay_location))
            night_events.append({
                "start": sunset.utc_iso(),
                "end": sunrise.utc_iso(),
                "display": "background",
                "className": "event-night",
            })

    return night_events
