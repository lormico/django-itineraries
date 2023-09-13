from typing import Optional

from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from loader.admin.models import localize, try_make_naive
from loader.models import Stay


@admin.register(Stay)
class StayAdmin(LeafletGeoAdmin):
    save_as = True

    def get_form(self, request, obj: Optional[Stay] = None, change=False, **kwargs):
        if request.method == "GET" and obj:
            lon, lat = obj.location.coords
            obj.checkin = try_make_naive(obj.checkin, lat, lon)
            obj.checkout = try_make_naive(obj.checkout, lat, lon)
            obj.cancel_before = try_make_naive(obj.cancel_before, lat, lon)
            # obj.payment_date = try_make_naive(obj.payment_date, lat, lon)
        form = super(StayAdmin, self).get_form(request, obj, change, **kwargs)
        return form

    def save_form(self, request, form, change):
        lat, lon = form.instance.latitude, form.instance.longitude
        form.instance.checkin = localize(form.instance.checkin, lat, lon)
        form.instance.checkout = localize(form.instance.checkout, lat, lon)
        form.instance.cancel_before = localize(form.instance.cancel_before, lat, lon)
        # form.instance.payment_date = localize(form.instance.payment_date, lat, lon)
        return super(StayAdmin, self).save_form(request, form, change)
