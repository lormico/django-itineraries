from datetime import datetime, timedelta
from typing import Dict, List

from skyfield import api, almanac

from data.admin.models import try_make_naive
from data.models import Stay

ts = api.load.timescale()
eph = api.load("de421.bsp")


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

    return stay_events + get_night_events(stays) + get_payment_events(stays) + get_cancel_before_events(stays)


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


def get_payment_events(stays):
    events = list()
    for stay in stays:
        events.append({
            "title": f"Pay {stay.formatted_price} to {stay.name} on {stay.website}",
            "start": stay.payment_date.isoformat(),
            "end": stay.payment_date.isoformat(),
            "allDay": True,
            "className": "event-payment",
        })

    return events


def get_cancel_before_events(stays):
    events = list()
    for stay in stays:
        events.append({
            "title": f"Last chance to cancel {stay.name} on {stay.website}!",
            "start": (stay.cancel_before - timedelta(hours=1)).isoformat(),
            "end": stay.cancel_before.isoformat(),
            "className": "event-cancel-before",
        })

    return events


def get_initial_date(events):
    # Returns the start date of the first future event
    # We don't bother with past payment events, for example
    sorted_events = sorted(events, key=lambda x: x["start"])
    initial_date = None
    for event in sorted_events:
        if datetime.fromisoformat(event["start"]) >= datetime.today():
            initial_date = event["start"]
            break

    return initial_date
