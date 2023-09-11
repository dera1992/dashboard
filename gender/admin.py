from import_export.admin import ImportExportModelAdmin
from .resource import GenderDistributionStateResource
from django.contrib import admin

from .models import GenderDistributionState

@admin.register(GenderDistributionState)
class GenderDistributionStateAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["abia", "adamawa","akwa_ibom", "anambra","created_at"]
    resource_class = GenderDistributionStateResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                GenderDistributionState.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)
