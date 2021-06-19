from rest_framework import generics
from route_planner.models import PollutionArea, Route
from route_planner.serializers import RouteSerializer, PollutionAreaSerializer
# Create your views here.


class ListCreateAreas(generics.ListCreateAPIView):
    queryset = PollutionArea.objects.all()
    serializer_class = PollutionAreaSerializer


class ListCreateRoute(generics.ListCreateAPIView):
    queryset = Route.objects.all()
    serializer_class = RouteSerializer
