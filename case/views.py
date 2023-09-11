# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import json

from django.shortcuts import render, redirect
from .models import CaseCategory, CaseStatus
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


def case_dashboard(request, category_slug=None):
    categorys = CaseCategory.objects.filter(is_active=True, current=True)

    for entry in categorys:
        data = (entry.inquiry_for_information, entry.inquiry_for_service, entry.hoax_call, entry.non_tb_calls,
                entry.appreciation_acknowledgement, entry.service_complaint, entry.technical_complaint, entry.covid_19,
                entry.suggestions, entry.dropped_calls, entry.test_calls,
        )

    status = CaseStatus.objects.filter(is_active=True, current=True)

    for ent in status:
        dat = (ent.open, ent.escalated, ent.pending, ent.resolved, ent.resolved_closed,
               )

    return render(request,'case/case_dashboard.html',{'catgorys': categorys,'status': status,
                                                      'cat': json.dumps(data),'sta': json.dumps(dat)})




