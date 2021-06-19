from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.


class PollutionArea(models.Model):
    class SatName(models.TextChoices):
        TROPOMI = "TR", _('TROPOMI')
        OMI = "OM", _('Omi')
        OTHER = "OT", _("Other")

    pollutant_concentration = models.FloatField(default=0.0)
    measured_at = models.DateTimeField(auto_now_add=True)
    source= models.CharField(
        max_length=2,
        choices=SatName.choices,
        default=SatName.TROPOMI
    )
    geometry = models.PolygonField(null=True,
                                   blank=True)

    def __str__(self):
        return self.source


class Route(models.Model):
    class RiskLevels(models.TextChoices):
        HIGH = 'HI', _('High')
        MEDIUM = 'MD', _('Medium')
        LOW = 'LO', _('Low')

    name = models.CharField(max_length=16, default="None")
    risk = models.CharField(
        max_length=2,
        choices=RiskLevels.choices,
        default=RiskLevels.HIGH
    )
    start_name = models.CharField(default="Parkeerplaats Duizendmeterweg", max_length=100)
    end_name= models.CharField(default="De Heuvel", max_length=100)

    start_geom = models.PointField(null=True,
                                   blank=True)
    end_geom = models.PointField(null=True,
                                 blank=True)
    geometry = models.LineStringField(null=True,
                                      blank=True)

    def __str__(self):
        return self.name