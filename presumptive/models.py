# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from home.models import TimeStampedModel, Call


class PresumptiveGenderDistribution(TimeStampedModel):
    presumptive_cases_tested = models.ForeignKey(Call, verbose_name=_('Presumptive cases tested based on Gender'), on_delete=models.CASCADE, null=True, blank=True, related_name="presumptive_cases_tested")
    presumptive_tested_positive = models.ForeignKey(Call, verbose_name=_('Presumptive who tested positive based on Gender'), on_delete=models.CASCADE, null=True, blank=True, related_name="presumptive_tested_positive")
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Presumptive Gender Distribution"
        verbose_name_plural = "Presumptive Gender Distributions"

class PresumptiveCasesTestedState(TimeStampedModel):
    abia = models.CharField(max_length=25, default=0)
    adamawa = models.CharField(max_length=25, default=0)
    akwa_ibom = models.CharField(max_length=25, default=0)
    anambra = models.CharField(max_length=25, default=0)
    bauchi = models.CharField(max_length=25, default=0)
    bayelsa = models.CharField(max_length=25, default=0)
    benue = models.CharField(max_length=25, default=0)
    borno = models.CharField(max_length=25, default=0)
    cross_river = models.CharField(max_length=25, default=0)
    delta = models.CharField(max_length=25, default=0)
    ebonyi = models.CharField(max_length=25, default=0)
    edo = models.CharField(max_length=25, default=0)
    ekiti = models.CharField(max_length=25, default=0)
    enugu = models.CharField(max_length=25, default=0)
    fct = models.CharField(max_length=25, default=0)
    gombe = models.CharField(max_length=25, default=0)
    imo = models.CharField(max_length=25, default=0)
    jigawa = models.CharField(max_length=25, default=0)
    kaduna = models.CharField(max_length=25, default=0)
    kano = models.CharField(max_length=25, default=0)
    kastina = models.CharField(max_length=25, default=0)
    kebbi = models.CharField(max_length=25, default=0)
    kogi = models.CharField(max_length=25, default=0)
    kwara = models.CharField(max_length=25, default=0)
    lagos = models.CharField(max_length=25, default=0)
    nassarawa = models.CharField(max_length=25, default=0)
    niger = models.CharField(max_length=25, default=0)
    ogun = models.CharField(max_length=25, default=0)
    ondo = models.CharField(max_length=25, default=0)
    osun = models.CharField(max_length=25, default=0)
    oyo = models.CharField(max_length=25, default=0)
    plateau = models.CharField(max_length=25, default=0)
    rivers = models.CharField(max_length=25, default=0)
    sokoto = models.CharField(max_length=25, default=0)
    taraba = models.CharField(max_length=25, default=0)
    yobe = models.CharField(max_length=25, default=0)
    zamfara = models.CharField(max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Presumptive cases tested by state"
        verbose_name_plural = "Presumptive cases tested by state"

    def __str__(self):
        return self.abia
