# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from home.models import TimeStampedModel, Caller

class InboundStatistics(TimeStampedModel):
    total_overall_calls = models.CharField("Total overall calls",max_length=25, default=0)
    calls_dropped_without = models.CharField("Calls dropped without opting for service",max_length=25, default=0)
    total_serviced_calls = models.CharField("Total Serviced calls",max_length=25, default=0)
    calls_self_service = models.CharField("Calls opted for self service",max_length=25, default=0)
    calls_opted_agent = models.CharField("Calls opted for agent",max_length=25, default=0)
    calls_received_agent = models.CharField("Calls received by agent",max_length=25, default=0)
    calls_opted_received = models.CharField("Calls opted for agent but not received",max_length=25, default=0)
    agent_received_serviced = models.CharField("Calls opted for agent but not received and not yet serviced",max_length=25, default=0)
    received_been_serviced = models.CharField("Calls opted for agent and not received but have been serviced",max_length=25, default=0)
    dropped_not_called_back  = models.CharField("Dropped after connecting to agent and has not been called back",max_length=25, default=0)
    dropped_called_back = models.CharField("Dropped after connecting to agent and has been called back",max_length=25, default=0)
    called_previous_month = models.CharField("Called Back and serviced (previous month)",
                                               max_length=25, default=0)
    called_review_month = models.CharField("Called Back and serviced (month in review)",
                                                    max_length=25, default=0)
    called_back_service = models.CharField("Called back and serviced",
                                               max_length=25, default=0)
    concluded_calls = models.CharField("Concluded calls to agent", max_length=25, default=0)
    total_referred_testing = models.CharField("Total callers referred for testing", max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Inbound Statistic"
        verbose_name_plural = "Inbound Statistics"

    def __str__(self):
        return self.total_overall_calls

class ActualUniqueCallers(TimeStampedModel):
    total_overall_calls = models.ForeignKey(Caller, on_delete=models.CASCADE, null=True, blank=True, related_name="total_overall_calls")
    total_serviced_calls = models.ForeignKey(Caller, on_delete=models.CASCADE, null=True, blank=True, related_name="total_serviced_calls")
    calls_self_service = models.ForeignKey(Caller, on_delete=models.CASCADE, null=True, blank=True, related_name="calls_self_service")
    calls_opted_agent = models.ForeignKey(Caller, on_delete=models.CASCADE, null=True, blank=True, related_name="calls_opted_agent")
    calls_received_agent = models.ForeignKey(Caller, on_delete=models.CASCADE, null=True, blank=True, related_name="calls_received_agent")
    calls_opted_received = models.ForeignKey(Caller, on_delete=models.CASCADE, null=True, blank=True, related_name="calls_opted_received")
    called_back_service = models.ForeignKey(Caller, on_delete=models.CASCADE, null=True, blank=True, related_name="called_back_service")
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Actual Calls Versus Unique Callers"
        verbose_name_plural = "Actual Calls Versus Unique Callers"

    def __str__(self):
        return str(self.total_overall_calls)

class PercentageInboundCalls(TimeStampedModel):
    eight = models.CharField("8:00-9:00", max_length=25, default=0)
    nine = models.CharField("9:00-10:00", max_length=25, default=0)
    ten = models.CharField("10:00-11:00", max_length=25, default=0)
    eleven = models.CharField("11:00-12:00", max_length=25, default=0)
    twelve = models.CharField("12:00-1:00", max_length=25, default=0)
    thirteen = models.CharField("1:00-2:00", max_length=25, default=0)
    fourteen = models.CharField("2:00-3.00", max_length=25, default=0)
    fifteen = models.CharField("3:00-4:00", max_length=25, default=0)
    sixteen = models.CharField("4:00-5:00", max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)
    class Meta:
        verbose_name = "Percentage (%) of Inbound Calls per Hour"
        verbose_name_plural = "Percentage (%) of Inbound Calls per Hour"

class CallsAbandonedIvr(TimeStampedModel):
    abandoned_ivr_within = models.CharField("Abandoned on IVR within Working Hour",max_length=25, default=0)
    abandoned_ivr_after = models.CharField("Abandoned on IVR After working Hour",max_length=25, default=0)
    abandoned_ivr_public = models.CharField("Abandoned on IVR on Public Holidays ",max_length=25, default=0)
    abandoned_ivr_weekend = models.CharField("Abandoned on IVR on Weekends",max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)
    class Meta:
        verbose_name = "Calls Abandoned on IVR Queue"
        verbose_name_plural = "Calls Abandoned on IVR Queue"