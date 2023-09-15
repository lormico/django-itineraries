from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from data.models import SideTrip


@admin.register(SideTrip)
class SideTripAdmin(LeafletGeoAdmin):
    save_as = True
