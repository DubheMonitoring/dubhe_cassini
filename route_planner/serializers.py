from rest_framework_gis.serializers import GeoFeatureModelSerializer
from route_planner.models import PollutionArea, Route, PollutionPoint


class PollutionAreaSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PollutionArea
        geo_field = "geometry"
        fields = "__all__"


class PollutionPointSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = PollutionPoint
        geo_field = "geometry"
        fields = "__all__"

class RouteSerializer(GeoFeatureModelSerializer):
    class Meta:
        model = Route
        geo_field="geometry"
        fields = "__all__"