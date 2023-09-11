from import_export.admin import ImportExportModelAdmin
from .resource import ReferralStatusResource, DetailedCallBreakdownResource, ReasonNotTestedResource
from django.contrib import admin

from .models import Call,Caller, ReferralStatus, DetailedCallBreakdown, ReasonNotTested

@admin.register(DetailedCallBreakdown)
class DetailedCallBreakdownAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["total_self_service_option", "indicate_speak_agent","services_provided_agent",
                    "dropped","hoax_call","created_at"]
    resource_class = ReferralStatusResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                DetailedCallBreakdown.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)

@admin.register(ReferralStatus)
class ReferralStatusAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["referred", "not_referred","created_at"]
    resource_class = DetailedCallBreakdownResource
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                ReferralStatus.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)

@admin.register(ReasonNotTested)
class ReasonNotTestedAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["relocated", "not_available","been_busy", "coughing_anymore","ask_to_pay", "sputum","created_at"]
    resource_class = ReasonNotTestedResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                ReasonNotTested.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)

admin.site.register(Call)
admin.site.register(Caller)