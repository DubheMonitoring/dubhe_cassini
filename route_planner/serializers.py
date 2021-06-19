from rest_framework import serializers
from route_planner.models import PollutionArea, Route


class PollutionAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PollutionArea
        fields = ('id', 'pollutant_concentration', 'measured_at', 'geometry')


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ('id', 'name', 'risk', 'start_name', 'end_name', 'start_geom', 'end_geom', 'geometry')