import pytz as pytz
from django.templatetags.static import static
from django.urls import reverse
from forex_python.converter import CurrencyRates

from jinja2 import Environment


# locale.setlocale(locale.LC_TIME, "it_IT")

currency_rates = CurrencyRates()


def jpy2eur(jpy):
    rate = currency_rates.get_rate("JPY", "EUR")
    return jpy * rate


def to_cet(value, fmt="%a %d/%m %H:%M %Z"):
    cet = pytz.timezone('Europe/Rome')
    local_dt = value.astimezone(cet)
    return local_dt.strftime(fmt)


def strftime(value):
    formatted = value.strftime("%a %d/%m %H:%M %Z")
    return formatted.replace("UTC+09:00", "JST")


def environment(**options):
    env = Environment(**options)
    env.globals.update(
        {
            "static": static,
            "url": reverse,
            "jpy2eur": jpy2eur,
        }
    )
    env.filters.update(
        {
            "to_cet": to_cet,
            "strftime": strftime,
        }
    )
    return env
