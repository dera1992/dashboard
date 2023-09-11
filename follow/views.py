# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render, redirect
from .models import FollowUpStatistics
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404,HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import date
from django.core.mail import EmailMessage



def followup_dashboard(request, category_slug=None):
    follows = FollowUpStatistics.objects.filter(is_active=True, current=True)

    y = list()
    for entry in follows:
        data = (entry.called_back, entry.responded, entry.disclosed_not_tested, entry.disclosed_tested,
                entry.disclosed_result, entry.disclosed_positive, entry.disclosed_negative, entry.gotten_result,
        )

    return render(request,'followup/followup_dashboard.html',{'follows': follows,"y": json.dumps(data)})



