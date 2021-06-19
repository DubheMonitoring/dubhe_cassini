from django.contrib import admin
from route_planner.models import PollutionArea


@admin.register(PollutionArea)
class PollutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'geometry')