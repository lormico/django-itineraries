from django.contrib.gis.serializers.geojson import Serializer as GeoJSONSerializer

DEFAULT_ICON = "https://maps.google.com/mapfiles/ms/micons/blue.png"


class Serializer(GeoJSONSerializer):

    def get_dump_object(self, obj):
        data = super().get_dump_object(obj)

        try:
            icon_url = obj.geomap_icon
        except AttributeError:
            icon_url = DEFAULT_ICON

        data["style"] = {
            "icon": {
                "iconUrl": icon_url,
                "iconSize": [32, 32],
                "iconAnchor": [16, 16]
            }}

        data["popupTemplate"] = "<strong>{name}</strong>"

        return data
