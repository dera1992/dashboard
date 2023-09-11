from django.urls import path
from . import views
from follow.views import followup_dashboard
from gender.views import GenderDistributionView
from geographical.views import GeographicalDistributionView
from hotline.views import HotlineView
from inbound.views import inbound_dashboard
from language.views import LanguageView
from presumptive.views import presumptive_dashboard
from case.views import case_dashboard

app_name = 'home'

urlpatterns = [
    path('', views.home, name='home'),
    path('inbound-dashboard/', inbound_dashboard, name='inbound-dashboard'),
    path('followup-dashboard/', followup_dashboard, name='followup-dashboard'),
    path('case-dashboard/', case_dashboard, name='case-dashboard'),
    path('hotline-dashboard/', HotlineView.as_view(), name='hotline-dashboard'),
    path('language-dashboard/', LanguageView.as_view(), name='language-dashboard'),
    path('geographic-dashboard/', GeographicalDistributionView.as_view(), name='geographic-dashboard'),
    path('gender-dashboard/', GenderDistributionView.as_view(), name='gender-dashboard'),
    path('presumptive-dashboard/', presumptive_dashboard, name='presumptive-dashboard'),

]