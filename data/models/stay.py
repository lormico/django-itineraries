from babel import numbers
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.utils.functional import classproperty

from data.models import Leg, Website


class Stay(models.Model):
    tranche = models.ForeignKey(Leg, on_delete=models.DO_NOTHING)
    id = models.CharField('ID', primary_key=True)
    name = models.CharField()
    checkin = models.DateTimeField('Check-in (local time)')
    checkout = models.DateTimeField('Check-out (local time)')
    price = models.FloatField()
    price_currency = models.CharField(default="JPY")
    website = models.ForeignKey(Website, on_delete=models.DO_NOTHING)
    cancel_before = models.DateTimeField('Cancel before (local time)')
    payment_date = models.DateField()
    location = models.PointField(geography=True, default=Point(0.0, 0.0))

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['tranche', 'id'], name='stay_pk'
            )
        ]
        ordering = ["checkin"]

    @property
    def geomap_icon(self):
        return "https://maps.google.com/mapfiles/ms/micons/lodging.png"

    @property
    def formatted_price(self):
        return numbers.format_currency(self.price, self.price_currency)

    @classproperty
    def layer_label(self):
        return "Stays"

    def __str__(self):
        return f"{self.name} ({self.website})"
