from import_export.admin import ImportExportModelAdmin
from .resource import SourceHotlineInformationResource
from django.contrib import admin

from .models import SourceHotlineInformation

@admin.register(SourceHotlineInformation)
class SourceHotlineInformationAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["radio", "tv", "friends_family", "handbill_posters",
                    "sms", "training_and_campaign","facebook_twitter_instagram",
                    "schools","ppmvs","religious_settings", "created_at"]
    resource_class = SourceHotlineInformationResource
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                SourceHotlineInformation.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)

