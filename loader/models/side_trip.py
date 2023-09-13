from django.db import models

from loader.models import Tranche
from loader.mixins import GeoItemModelMixin


class SideTrip(GeoItemModelMixin):
    tranche = models.ForeignKey(Tranche, on_delete=models.DO_NOTHING)
    id = models.CharField('ID', primary_key=True)
    name = models.CharField()
    date = models.DateField()

    @property
    def geomap_icon(self):
        return "https://maps.google.com/mapfiles/ms/micons/hiker.png"

    def __str__(self):
        return f"{self.name}"
