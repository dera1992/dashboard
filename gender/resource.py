from import_export import resources
from import_export.fields import Field
from .models import GenderDistributionState


class GenderDistributionStateResource(resources.ModelResource):

     class Meta:
         model = GenderDistributionState
         exclude = ('is_active','modified_at','created_by','created_at','modified_by','current', )
