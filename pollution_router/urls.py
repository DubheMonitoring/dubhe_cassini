"""pollution_router URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from route_planner.views import ListCreateAreas, ListCreateRoute, ListCreatePoints
urlpatterns = [
    path('admin/', admin.site.urls),
url(r'^api/areas', ListCreateAreas.as_view(), name='list_areas'),
url(r'^api/routes', ListCreateRoute.as_view(), name='list_areas'),
url(r'^api/points', ListCreatePoints.as_view(), name='list_areas')
]
