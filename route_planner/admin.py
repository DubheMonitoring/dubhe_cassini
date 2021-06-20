from django.contrib.gis import admin
from route_planner.models import PollutionArea, Route, PollutionPoint


@admin.register(PollutionArea)
class PollutionAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'geometry')


@admin.register(Route)
class RouteAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'risk', 'start_name', 'end_name', 'geometry')


@admin.register(PollutionPoint)
class PointAdmin(admin.OSMGeoAdmin):
    list_display = ('locationid', 'pollutant_concentration', 'measured_at', 'geometry')


class LocationAdmin(admin.OSMGeoAdmin):
    default_zoom = 5


class LocationAdmin(admin.OSMGeoAdmin):
    point_zoom = 10
