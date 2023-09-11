# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from home.models import TimeStampedModel

class FollowUpStatistics(TimeStampedModel):
    called_back = models.CharField("Presumptive cases called back",max_length=25, default=0)
    responded = models.CharField("Presumptive cases responded (reached?)",max_length=25, default=0)
    disclosed_not_tested = models.CharField("Presumptive cases reached who disclosed not tested",max_length=25, default=0)
    disclosed_tested = models.CharField("Presumptive cases reached who disclosed tested",max_length=25, default=0)
    disclosed_result = models.CharField("Presumptive cases reached who did not disclose result",max_length=25, default=0)
    disclosed_positive = models.CharField("Presumptive cases reached who disclosed Positive",max_length=25, default=0)
    disclosed_negative = models.CharField("Presumptive cases reached who disclosed Negative",max_length=25, default=0)
    gotten_result = models.CharField("Presumptive cases reached who has not gotten result",max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)


    class Meta:
        verbose_name = "Follow Up Statistics"
        verbose_name_plural = "Follow Up Statistics"

    def __str__(self):
        return self.called_back
