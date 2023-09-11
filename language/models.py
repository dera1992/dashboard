# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from home.models import TimeStampedModel

class LanguageSelection(TimeStampedModel):
    english = models.CharField(max_length=25, default=0)
    pidgin = models.CharField(max_length=25, default=0)
    hausa = models.CharField(max_length=25, default=0)
    yoruba = models.CharField(max_length=25, default=0)
    igbo = models.CharField(max_length=25, default=0)
    current = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name = "Language Selection"
        verbose_name_plural = "Language Selection"

    def __str__(self):
        return self.english
