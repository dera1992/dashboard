from import_export.admin import ImportExportModelAdmin
from .resource import FollowUpStatisticsResource
from django.contrib import admin

from .models import FollowUpStatistics

@admin.register(FollowUpStatistics)
class FollowUpStatisticsAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["called_back", "responded", "disclosed_not_tested",
                    "disclosed_tested", "disclosed_result", "disclosed_positive",
                    "disclosed_negative","gotten_result","created_at"]
    resource_class = FollowUpStatisticsResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                FollowUpStatistics.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)