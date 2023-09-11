# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from home.models import Call,TimeStampedModel


class GenderDistributionState(TimeStampedModel):
    abia = models.ForeignKey(Call, verbose_name=_('Abia'), on_delete=models.CASCADE, null=True, blank=True,related_name="abia")
    adamawa = models.ForeignKey(Call, verbose_name=_('Adamawa'), on_delete=models.CASCADE,null=True, blank=True,related_name="adamawa")
    akwa_ibom = models.ForeignKey(Call, verbose_name=_('Akwa Ibom'), on_delete=models.CASCADE, null=True, blank=True,related_name="akwa_ibom")
    anambra = models.ForeignKey(Call, verbose_name=_('Anambra'), on_delete=models.CASCADE, null=True, blank=True,related_name="anambra")
    bauchi = models.ForeignKey(Call, verbose_name=_('Bauchi'), on_delete=models.CASCADE, null=True, blank=True,related_name="bauchi")
    bayelsa = models.ForeignKey(Call, verbose_name=_('Bayelsa'), on_delete=models.CASCADE, null=True, blank=True,related_name="bayelsa")
    benue = models.ForeignKey(Call, verbose_name=_('Benue'), on_delete=models.CASCADE, null=True, blank=True,related_name="benue")
    borno = models.ForeignKey(Call, verbose_name=_('Borno'), on_delete=models.CASCADE, null=True, blank=True,related_name="borno")
    cross_river = models.ForeignKey(Call, verbose_name=_('Cross River'), on_delete=models.CASCADE, null=True, blank=True,related_name="cross_river")
    delta = models.ForeignKey(Call, verbose_name=_('Delta'), on_delete=models.CASCADE, null=True, blank=True,related_name="delta")
    ebonyi = models.ForeignKey(Call, verbose_name=_('Ebonyi'), on_delete=models.CASCADE, null=True, blank=True, related_name="ebonyi")
    edo = models.ForeignKey(Call, verbose_name=_('Edo'), on_delete=models.CASCADE, null=True, blank=True,related_name="edo")
    ekiti = models.ForeignKey(Call, verbose_name=_('Ekiti'), on_delete=models.CASCADE, null=True, blank=True,related_name="ekiti")
    enugu = models.ForeignKey(Call, verbose_name=_('Enugu'), on_delete=models.CASCADE, null=True, blank=True,related_name="enugu")
    fct = models.ForeignKey(Call, verbose_name=_('FCT'), on_delete=models.CASCADE, null=True, blank=True,related_name="fct")
    gombe = models.ForeignKey(Call, verbose_name=_('Gombe'), on_delete=models.CASCADE, null=True, blank=True,related_name="gombe")
    imo = models.ForeignKey(Call, verbose_name=_('Imo'), on_delete=models.CASCADE, null=True, blank=True,related_name="imo")
    jigawa = models.ForeignKey(Call, verbose_name=_('Jigawa'), on_delete=models.CASCADE, null=True, blank=True,related_name="jigawa")
    kaduna = models.ForeignKey(Call, verbose_name=_('Kaduna'), on_delete=models.CASCADE, null=True, blank=True,related_name="kaduna")
    kano = models.ForeignKey(Call, verbose_name=_('Kano'), on_delete=models.CASCADE, null=True, blank=True,related_name="kano")
    kastina = models.ForeignKey(Call, verbose_name=_('Kastina'), on_delete=models.CASCADE, null=True, blank=True,related_name="kastina")
    kebbi = models.ForeignKey(Call, verbose_name=_('Kebbi'), on_delete=models.CASCADE, null=True, blank=True,related_name="kebbi")
    kogi = models.ForeignKey(Call, verbose_name=_('Kogi'), on_delete=models.CASCADE, null=True, blank=True,related_name="kogi")
    kwara = models.ForeignKey(Call, verbose_name=_('Kwara'), on_delete=models.CASCADE, null=True, blank=True,related_name="kwara")
    lagos = models.ForeignKey(Call, verbose_name=_('Lagos'), on_delete=models.CASCADE, null=True, blank=True,related_name="lagos")
    nassarawa = models.ForeignKey(Call, verbose_name=_('Nassarawa'), on_delete=models.CASCADE, null=True, blank=True,related_name="nassarawa")
    niger = models.ForeignKey(Call, verbose_name=_('Niger'), on_delete=models.CASCADE, null=True, blank=True,related_name="niger")
    ogun = models.ForeignKey(Call, verbose_name=_('Ogun'), on_delete=models.CASCADE, null=True, blank=True,related_name="ogun")
    ondo = models.ForeignKey(Call, verbose_name=_('Ondo'), on_delete=models.CASCADE, null=True, blank=True,related_name="ondo")
    osun = models.ForeignKey(Call, verbose_name=_('Osun'), on_delete=models.CASCADE, null=True, blank=True,related_name="osun")
    oyo = models.ForeignKey(Call, verbose_name=_('Oyo'), on_delete=models.CASCADE, null=True, blank=True,related_name="oyo")
    plateau = models.ForeignKey(Call, verbose_name=_('Plateau'), on_delete=models.CASCADE, null=True, blank=True,related_name="plateau")
    rivers = models.ForeignKey(Call, verbose_name=_('Rivers'), on_delete=models.CASCADE, null=True, blank=True,related_name="rivers")
    sokoto = models.ForeignKey(Call, verbose_name=_('Sokoto'), on_delete=models.CASCADE, null=True, blank=True,related_name="sokoto")
    taraba = models.ForeignKey(Call, verbose_name=_('Taraba'), on_delete=models.CASCADE, null=True, blank=True,related_name="taraba")
    yobe = models.ForeignKey(Call, verbose_name=_('Yobe'), on_delete=models.CASCADE, null=True, blank=True,related_name="yobe")
    zamfara = models.ForeignKey(Call, verbose_name=_('Zamfara'), on_delete=models.CASCADE, null=True, blank=True,related_name="zamfara")
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Gender Distribution by State"
        verbose_name_plural = "Gender Distribution by States"

    def __str__(self):
        return str(self.abia)
