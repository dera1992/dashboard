from import_export.admin import ImportExportModelAdmin
from .resource import CaseCategoryResource, CaseStatusResource
from django.contrib import admin

from .models import CaseStatus,CaseCategory

@admin.register(CaseStatus)
class CaseStatusAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["open", "escalated", "pending","resolved", "escalated", "resolved_closed","created_at"]
    resource_class = CaseStatusResource

    def save_model(self, request, obj, form, change):

        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                CaseStatus.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)

@admin.register(CaseCategory)
class CaseCategoryAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["inquiry_for_information", "inquiry_for_service", "hoax_call", "non_tb_calls",
                    "appreciation_acknowledgement", "service_complaint", "created_at"]
    resource_class = CaseCategoryResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                CaseCategory.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)