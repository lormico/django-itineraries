from django.contrib.gis.db import models
from django.contrib.gis.geos import Point

from loader.models import Tranche


class SideTrip(models.Model):
    tranche = models.ForeignKey(Tranche, on_delete=models.DO_NOTHING)
    id = models.CharField('ID', primary_key=True)
    name = models.CharField()
    date = models.DateField()
    location = models.PointField(geography=True, default=Point(0.0, 0.0))

    @property
    def geomap_icon(self):
        return "https://maps.google.com/mapfiles/ms/micons/hiker.png"

    def __str__(self):
        return f"{self.name}"
