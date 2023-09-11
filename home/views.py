# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render, redirect
from .models import Call, DetailedCallBreakdown
from inbound.models import InboundStatistics, ActualUniqueCallers, PercentageInboundCalls, CallsAbandonedIvr
from follow.models import FollowUpStatistics
from case.models import CaseCategory, CaseStatus
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


def home(request, category_slug=None):
    overall_list = []
    overall_calls = ActualUniqueCallers.objects.filter(current=True)
    if overall_calls:
        call = overall_calls[0]
        overall_list.append(call)
    else:
        overall_list = []
    actual_calls = ActualUniqueCallers.objects.filter(current=True)

    for entry in actual_calls:
        data = (entry.total_overall_calls.actual_callers,entry.total_serviced_calls.actual_callers, entry.calls_self_service.actual_callers,
                entry.calls_opted_agent.actual_callers, entry.calls_received_agent.actual_callers,entry.calls_opted_received.actual_callers,
                entry.called_back_service.actual_callers)
        dat = (entry.total_overall_calls.unique_callers, entry.total_serviced_calls.unique_callers,
                entry.calls_self_service.unique_callers,
                entry.calls_opted_agent.unique_callers, entry.calls_received_agent.unique_callers,
                entry.calls_opted_received.unique_callers,
                entry.called_back_service.unique_callers)

    serviced_calls = InboundStatistics.objects.filter(is_active=True, current=True)
    first_calls = DetailedCallBreakdown.objects.filter(is_active=True, current=True)
    referred_testing = InboundStatistics.objects.filter(is_active=True, current=True)
    called_back = FollowUpStatistics.objects.filter(is_active=True, current=True)
    categorys = CaseCategory.objects.filter(is_active=True, current=True)

    for entry in categorys:
        datas = (entry.inquiry_for_information, entry.inquiry_for_service, entry.hoax_call, entry.non_tb_calls,
                entry.appreciation_acknowledgement, entry.service_complaint, entry.technical_complaint, entry.covid_19,
                entry.suggestions, entry.dropped_calls, entry.test_calls,
                )

    return render(request,'home/index.html', {'overall_calls': overall_calls,'overall_list': overall_list,'serviced_calls':serviced_calls,
                                              'first_calls':first_calls,'referred_testing': referred_testing,
                                              'called_back':called_back,'actual_calls':actual_calls,"y": json.dumps(data),
                                              "x": json.dumps(dat),"case": json.dumps(datas)})



