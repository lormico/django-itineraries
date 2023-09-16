from rest_framework.serializers import HyperlinkedModelSerializer
from rest_framework_gis.serializers import GeoFeatureModelListSerializer, GeoFeatureModelSerializer

from data.models import Leg, SideTrip, Stay, Website

DEFAULT_ICON = "https://maps.google.com/mapfiles/ms/micons/blue.png"


class LeafletFeatureListSerializer(GeoFeatureModelListSerializer):

    def to_representation(self, data):
        feature_list = super().to_representation(data)

        try:
            layer_label = data.model.layer_label
        except AttributeError:
            layer_label = "Layer"

        feature_list["layerLabel"] = layer_label

        return feature_list


class GeoFeatureModelCssSerializer(GeoFeatureModelSerializer):

    def to_representation(self, instance):
        feature = super().to_representation(instance)

        try:
            icon_url = instance.geomap_icon
        except AttributeError:
            icon_url = DEFAULT_ICON

        feature["style"] = {
            "icon": {
                "iconUrl": icon_url,
                "iconSize": [32, 32],
                "iconAnchor": [16, 16]
            }}

        feature["popupTemplate"] = "<strong>{name}</strong>"

        return feature


class LegSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Leg
        fields = "__all__"


class SideTripSerializer(GeoFeatureModelCssSerializer):
    class Meta:
        model = SideTrip
        list_serializer_class = LeafletFeatureListSerializer
        geo_field = "location"
        fields = "__all__"


class StaySerializer(GeoFeatureModelCssSerializer):
    class Meta:
        model = Stay
        list_serializer_class = LeafletFeatureListSerializer
        geo_field = "location"
        fields = "__all__"


class WebsiteSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Website
        fields = "__all__"
