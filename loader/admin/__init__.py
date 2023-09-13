from django.contrib import admin
from django_admin_geomap import ModelAdmin

from loader.models import Tranche, Website, SideTrip


class GeoAdmin(ModelAdmin):
    geomap_autozoom = 10
    geomap_field_longitude = "id_longitude"
    geomap_field_latitude = "id_latitude"


admin.site.register(Tranche)
admin.site.register(Website)

from .models.side_trip import SideTripAdmin
from .models.stay import StayAdmin

# admin.site.register(Stay, GeoAdmin)
