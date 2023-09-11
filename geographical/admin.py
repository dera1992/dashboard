from import_export.admin import ImportExportModelAdmin
from .resource import GeographicalDistributionResource, GenderGeographicalResource
from django.contrib import admin

from .models import GeographicalDistribution, GenderGeographical

@admin.register(GeographicalDistribution)
class GeographicalDistributionAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["north_west", "north_east", "north_central", "south_south",
                    "south_east", "south_west", "created_at"]
    resource_class = GeographicalDistributionResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                GeographicalDistribution.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)

@admin.register(GenderGeographical)
class GenderGeographicalAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ["north_west", "north_east", "north_central", "south_south",
                    "south_east", "south_west", "created_at"]
    resource_class = GenderGeographicalResource

    def save_model(self, request, obj, form, change):
        if request.user.is_superuser:
            if obj.is_active:
                obj.current = True
                GenderGeographical.objects.filter(is_active=True).update(
                    current=False
                )
                super().save_model(request, obj, form, change)
            else:
                return super().save_model(request, obj, form, change)
        else:
            return super().save_model(request, obj, form, change)