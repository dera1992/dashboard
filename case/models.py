# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from home.models import TimeStampedModel


class CaseCategory(TimeStampedModel):
    inquiry_for_information =models.CharField( max_length=25, default=0)
    inquiry_for_service = models.CharField(max_length=25, default=0)
    hoax_call = models.CharField(max_length=25, default=0)
    non_tb_calls = models.CharField("Non-TB Calls",max_length=25, default=0)
    appreciation_acknowledgement = models.CharField("Appreciation/Acknowledgement",max_length=25, default=0)
    service_complaint = models.CharField(max_length=25, default=0)
    technical_complaint = models.CharField(max_length=25, default=0)
    covid_19 = models.CharField("Covid-19",max_length=25, default=0)
    suggestions = models.CharField(max_length=25, default=0)
    dropped_calls = models.CharField(max_length=25, default=0)
    test_calls = models.CharField(max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Case Category"
        verbose_name_plural = "Case Categories"

    def __str__(self):
        return self.inquiry_for_information

class CaseStatus(TimeStampedModel):
    open = models.CharField(max_length=25, default=0)
    escalated = models.CharField(max_length=25, default=0)
    pending = models.CharField(max_length=25, default=0)
    resolved = models.CharField(max_length=25, default=0)
    resolved_closed = models.CharField(max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Case Status"
        verbose_name_plural = "Case Status"

    def __str__(self):
        return self.open