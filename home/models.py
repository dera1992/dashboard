# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from home.constants import BASE_READ_ONLY_FIELDS



class TimeStampedModel(models.Model):
    """
    An abstract base class model that provides self updating
    ``created_at`` and ``modified_at`` fields.
    """
    READ_ONLY_FIELDS = BASE_READ_ONLY_FIELDS
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='%(app_label)s_%(class)s_created_by')
    modified_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                   null=True, blank=True, on_delete=models.SET_NULL,
                                   related_name='%(app_label)s_%(class)s_updated_by')

    class Meta:
        abstract = True

    def save_model(self, request, obj, form, change):
        pass

class Caller(TimeStampedModel):
    actual_callers = models.CharField(max_length=25, default=0)
    unique_callers = models.CharField(max_length=25, default=0)

    class Meta:
        verbose_name = "Caller"
        verbose_name_plural = "Callers"

    def __str__(self):
        return "{} {}".format("Actual " + str(self.actual_callers), "Unique " + str(self.unique_callers))

class Call(TimeStampedModel):
    male = models.CharField(max_length=25, default=0)
    female = models.CharField(max_length=25, default=0)

    class Meta:
        verbose_name = "Call"
        verbose_name_plural = "Calls"

    def __str__(self):
        return "{} {}".format("male " + str(self.male), "female " + str(self.female))


class ReferralStatus(TimeStampedModel):
    referred = models.CharField( max_length=25, default=0)
    not_referred = models.CharField(max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Referral Status"
        verbose_name_plural = "Referral Status"

    def __str__(self):
        return self.referred

class DetailedCallBreakdown(TimeStampedModel):
    total_self_service_option = models.CharField("Total No. of callers that used the Self-Service Option for referral",max_length=25, default=0)
    indicate_speak_agent = models.CharField("Total No. of Callers that indicated to speak with an Agent",max_length=25, default=0)
    services_provided_agent = models.CharField("TB Services provided by Agent at first call ",max_length=25, default=0)
    dropped = models.CharField("Dropped",max_length=25, default=0)
    hoax_call = models.CharField("Hoax Calls",max_length=25, default=0)
    test_call = models.CharField("Test Calls",max_length=25, default=0)
    calls_connected_agent = models.CharField("Total No. of calls connected to an Agent",max_length=25, default=0)
    calls_abandoned_agent = models.CharField("Total No. of calls abandoned on Agent Queue",max_length=25, default=0)
    abandoned_ivr_working_hour = models.CharField("Abandoned on IVR within Working Hour",max_length=25, default=0)
    abandoned_ivr_after_work = models.CharField("Abandoned on IVR After working Hour",max_length=25, default=0)
    abandoned_ivr_public_holiday = models.CharField("Abandoned on IVR on Public Holidays",max_length=25, default=0)
    abandoned_ivr_weekend = models.CharField("Abandoned on IVR on Weekends",
                                               max_length=25, default=0)
    abandoned_welcome_ivr_not_speak = models.CharField("Total No. of calls abandoned on welcome IVR and has not indicated to speak with an Agent",
                                                    max_length=25, default=0)
    calls_abandoned_ivr_callers = models.CharField("Calls abandoned on IVR by Callers",
                                               max_length=25, default=0)
    calls_abandoned_ivr_wrong_service = models.CharField("Calls Abandoned on IVR due to wrong Service Selection", max_length=25, default=0)
    calls_abandoned_ivr_no_service = models.CharField("Calls Abandoned on IVR due to no Service Selection", max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Detailed Call Breakdown"
        verbose_name_plural = "Detailed Call Breakdown"

    def __str__(self):
        return self.total_self_service_option

class ReasonNotTested(TimeStampedModel):
    relocated =models.CharField("Relocated to another state",max_length=25, default=0)
    not_available = models.CharField("Health workers were not available",max_length=25, default=0)
    been_busy = models.CharField("I have been busy",max_length=25, default=0)
    coughing_anymore = models.CharField("Not coughing anymore",max_length=25, default=0)
    ask_to_pay = models.CharField("I was asked to pay for test",max_length=25, default=0)
    sputum = models.CharField("Could not cough up sputum",max_length=25, default=0)
    locate_address = models.CharField("Could not locate the address",max_length=25, default=0)
    tools_testing = models.CharField("They do not have tools for testing",max_length=25, default=0)
    coughing_relative = models.CharField("I am not the one coughing it was my relative/Friend",max_length=25, default=0)
    travelled = models.CharField("I travelled",max_length=25, default=0)
    therapy = models.CharField("On a therapy",max_length=25, default=0)
    no_money = models.CharField("No money for card/Transport", max_length=25, default=0)
    person_died = models.CharField("The person died", max_length=25, default=0)
    afraid_stress = models.CharField("Afraid of Stress/Not Strong/crowd at the health facility", max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Reasons for not getting tested by States"
        verbose_name_plural = "Reasons for not getting tested by States"

    def __str__(self):
        return self.relocated


