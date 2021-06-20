import shapely.wkt
from rest_framework import generics
import geojson
from route_planner.models import PollutionArea, Route, PollutionPoint
from route_planner.serializers import RouteSerializer, PollutionAreaSerializer, PollutionPointSerializer
from shapely.geometry import Point, LineString
import geocoder
from openrouteservice import client, directions
from openrouteservice import convert
from shapely.geometry import shape
import yaml

# Create your views here.
### DELETE BEFORE PUSHING ###
APIKEY = ""


class ListCreateAreas(generics.ListCreateAPIView):
    queryset = PollutionArea.objects.all()
    serializer_class = PollutionAreaSerializer


class ListCreatePoints(generics.ListCreateAPIView):
    queryset = PollutionPoint.objects.all()
    serializer_class = PollutionPointSerializer


class ListCreateRoute(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer

    def perform_create(self, serializer):
        address_start = serializer.initial_data['start_name']
        address_end = serializer.initial_data['end_name']
        start_g = geocoder.osm(address_start)
        start_lat, start_lon = start_g.latlng
        pnt_start = Point(start_lon, start_lat)
        end_g = geocoder.osm(address_end)
        end_lat, end_lon = end_g.latlng
        pnt_end = Point(end_lon, end_lat)
        line = LineString([pnt_start, pnt_end]).wkt
        pnt_start = pnt_start.wkt
        pnt_end = pnt_end.wkt
        clnt = client.Client(key=APIKEY)
        geometry = directions.directions(clnt, ((start_lon, start_lat), (end_lon, end_lat)))['routes'][0]['geometry']
        decoded = convert.decode_polyline(geometry)
        line = shape(decoded).wkt
        geom = shapely.wkt.loads(line)
        serializer.save(start_geom=pnt_start, end_geom=pnt_end, geometry=line)
