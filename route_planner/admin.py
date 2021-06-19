from django.contrib.gis import admin
from route_planner.models import PollutionArea, Route


@admin.register(PollutionArea)
class PollutionAdmin(admin.OSMGeoAdmin):
    list_display = ('id', 'geometry')


@admin.register(Route)
class RouteAdmin(admin.OSMGeoAdmin):
    list_display = ('name', 'risk', 'start_name', 'end_name', 'geometry')


class LocationAdmin(admin.OSMGeoAdmin):
    default_zoom = 5

class LocationAdmin(admin.OSMGeoAdmin):
    point_zoom = 10
