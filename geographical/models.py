# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from home.models import TimeStampedModel, Call

class GeographicalDistribution(TimeStampedModel):
    north_west = models.CharField( max_length=50)
    north_east = models.CharField(max_length=50)
    north_central = models.CharField(max_length=50)
    south_south = models.CharField(max_length=50)
    south_east = models.CharField(max_length=50)
    south_west = models.CharField(max_length=50)
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Geographical Distribution"
        verbose_name_plural = "Geographical Distribution"

    def __str__(self):
        return self.north_west

class GenderGeographical(TimeStampedModel):
    north_west = models.ForeignKey(Call, on_delete=models.CASCADE, null=True, blank=True, related_name="north_west")
    north_east = models.ForeignKey(Call, on_delete=models.CASCADE, null=True, blank=True,related_name="north_east")
    north_central = models.ForeignKey(Call, on_delete=models.CASCADE, null=True, blank=True, related_name="north_central")
    south_south = models.ForeignKey(Call, on_delete=models.CASCADE, null=True, blank=True, related_name="south_south")
    south_east = models.ForeignKey(Call, on_delete=models.CASCADE, null=True, blank=True, related_name="south_east")
    south_west = models.ForeignKey(Call, on_delete=models.CASCADE, null=True, blank=True, related_name="south_west")
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Gender by Geopolitical Zones"
        verbose_name_plural = "Gender by Geopolitical Zones"

    def __str__(self):
        return f"{self.north_west}"
