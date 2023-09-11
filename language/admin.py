from import_export.admin import ImportExportModelAdmin
from .resource import LanguageSelectionResource
from django.contrib import admin

from .models import LanguageSelection


@admin.register(LanguageSelection)
class LanguageSelectionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["english", "pidgin", "hausa", "yoruba",
                    "igbo","created_at"]
    resource_class = LanguageSelectionResource
    
    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                LanguageSelection.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)
            

