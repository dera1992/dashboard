# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from home.models import TimeStampedModel

class SourceHotlineInformation(TimeStampedModel):
    radio = models.CharField(max_length=25, default=0)
    tv = models.CharField(max_length=25, default=0)
    friends_family = models.CharField(max_length=25, default=0)
    handbill_posters = models.CharField(max_length=25, default=0)
    sms = models.CharField(max_length=25, default=0)
    training_and_campaign = models.CharField(max_length=25, default=0)
    facebook_twitter_instagram = models.CharField(max_length=25, default=0)
    schools = models.CharField(max_length=25, default=0)
    ppmvs = models.CharField(max_length=25, default=0)
    religious_settings = models.CharField(max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Source Hotline Information"
        verbose_name_plural = "Source Hotline Information"

    def __str__(self):
        return self.radio
