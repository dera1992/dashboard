from import_export.admin import ImportExportModelAdmin
from .resource import PresumptiveGenderDistributionResource, PresumptiveCasesTestedStateResource
from django.contrib import admin

from .models import PresumptiveGenderDistribution,PresumptiveCasesTestedState

@admin.register(PresumptiveGenderDistribution)
class PresumptiveGenderDistributionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["presumptive_cases_tested", "presumptive_tested_positive","created_at"]
    resource_class = PresumptiveGenderDistributionResource

@admin.register(PresumptiveCasesTestedState)
class PresumptiveCasesTestedStateAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["abia", "adamawa","akwa_ibom", "anambra","created_at"]
    resource_class = PresumptiveCasesTestedStateResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                PresumptiveCasesTestedState.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)
