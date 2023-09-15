from django.contrib import admin

from data.models import Tranche, Website

admin.site.register(Tranche)
admin.site.register(Website)

from .models.side_trip import SideTripAdmin
from .models.stay import StayAdmin

# admin.site.register(Stay, GeoAdmin)
