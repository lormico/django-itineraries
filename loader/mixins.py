from django.db import models
from django_admin_geomap import GeoItem


class GeoItemModelMixin(models.Model, GeoItem):
    latitude = models.FloatField()
    longitude = models.FloatField()

    @property
    def geomap_latitude(self):
        return str(self.latitude)

    @property
    def geomap_longitude(self):
        return str(self.longitude)

    class Meta:
        abstract = True
