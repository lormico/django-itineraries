from django.contrib import admin

from loader.admin import GeoAdmin
from loader.models import SideTrip


@admin.register(SideTrip)
class SideTripAdmin(GeoAdmin):
    save_as = True
