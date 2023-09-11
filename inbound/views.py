# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render, redirect
from .models import InboundStatistics, ActualUniqueCallers, PercentageInboundCalls, CallsAbandonedIvr
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

def inbound_dashboard(request, category_slug=None):
    inbounds = InboundStatistics.objects.filter(is_active=True, current=True)
    # inbound_data = {"name": "Inbound Statistics", "data": []}

    y = list()
    for entry in inbounds:
        data = (entry.total_overall_calls,entry.calls_dropped_without, entry.total_serviced_calls, entry.calls_self_service,
                entry.calls_opted_agent, entry.calls_received_agent, entry.calls_opted_received,entry.agent_received_serviced,
                entry.received_been_serviced,entry.dropped_not_called_back,entry.dropped_called_back,entry.called_previous_month,
                entry.called_review_month,entry.called_back_service,entry.concluded_calls,entry.total_referred_testing)

    actuals = ActualUniqueCallers.objects.filter(is_active=True, current=True)
    percentages = PercentageInboundCalls.objects.filter(is_active=True, current=True)
    calls = CallsAbandonedIvr.objects.filter(is_active=True, current=True)
    return render(request,'inbound/inbound_dashboard.html', {'inbounds': inbounds,'actuals': actuals,'percentages':percentages,
                                              'calls':calls,"y": json.dumps(data),})


