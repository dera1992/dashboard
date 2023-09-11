from import_export.admin import ImportExportModelAdmin
from .resource import InboundStatisticsResource, ActualUniqueCallersResource, PercentageInboundCallsResource, CallsAbandonedIvrResource
from django.contrib import admin

from .models import InboundStatistics,ActualUniqueCallers, PercentageInboundCalls, CallsAbandonedIvr

@admin.register(InboundStatistics)
class InboundStatisticsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["total_overall_calls", "calls_dropped_without", "total_serviced_calls",
                    "calls_self_service", "calls_opted_agent", "calls_received_agent",
                    "calls_opted_received","agent_received_serviced","created_at"]
    resource_class = InboundStatisticsResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                InboundStatistics.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)

@admin.register(ActualUniqueCallers)
class ActualUniqueCallersAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["total_overall_calls", "total_serviced_calls", "calls_self_service",
                    "calls_opted_agent", "calls_received_agent", "calls_opted_received",
                    "called_back_service","created_at"]
    resource_class = ActualUniqueCallersResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                ActualUniqueCallers.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)

@admin.register(PercentageInboundCalls)
class PercentageInboundCallsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["eight", "nine", "ten",
                    "eleven", "twelve", "thirteen",
                    "fourteen","fifteen","created_at"]
    resource_class = PercentageInboundCallsResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                PercentageInboundCalls.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)

@admin.register(CallsAbandonedIvr)
class CallsAbandonedIvrAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["abandoned_ivr_within", "abandoned_ivr_after", "abandoned_ivr_public",
                    "abandoned_ivr_weekend","created_at"]
    resource_class = CallsAbandonedIvrResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                CallsAbandonedIvr.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)