# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect, Http404,HttpResponse, JsonResponse
from django.contrib.auth.models import User
from .models import LanguageSelection
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.views.decorators.http import require_POST
from django.views import generic
from django.utils import timezone
from datetime import date
from django.core.mail import EmailMessage

#def language_dashboard(request):
    #return render(request, 'language/language_dashboard.html')
    
    
class LanguageView(generic.TemplateView):
    template_name = 'language/language_dashboard.html'   
    
    def get_context_data(self, **kwargs):
        context = super(LanguageView, self).get_context_data(**kwargs)
        languages = LanguageSelection.objects.filter(current=True)
        
        context.update({
            "languages": languages
        })
        return context
                
                
                
        
        
                
        
                
            
            
        



