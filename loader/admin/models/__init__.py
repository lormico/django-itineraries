from zoneinfo import ZoneInfo

from django.utils import timezone
from django.utils.timezone import is_naive
from timezonefinder import TimezoneFinder

tf = TimezoneFinder()


def localize(datetime, lat, lon):
    tzname = tf.timezone_at(lat=lat, lng=lon)
    return datetime.replace(tzinfo=ZoneInfo(tzname))


def try_make_naive(datetime, lat, lon):
    if is_naive(datetime):
        return datetime
    tzname = tf.timezone_at(lat=lat, lng=lon)
    return timezone.make_naive(datetime, ZoneInfo(tzname))
