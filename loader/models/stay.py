from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from loader.models import Tranche, Website


class Stay(models.Model):
    tranche = models.ForeignKey(Tranche, on_delete=models.DO_NOTHING)
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

    def __str__(self):
        return f"{self.name} ({self.website})"
