from import_export import resources
from import_export.fields import Field
from .models import PresumptiveGenderDistribution, PresumptiveCasesTestedState

class PresumptiveGenderDistributionResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Id')
    presumptive_cases_tested__male = Field(attribute='presumptive_cases_tested__male', column_name='Presumptive cases tested based on Gender(Male)')
    presumptive_cases_tested__female = Field(attribute='presumptive_cases_tested__female', column_name='Presumptive cases tested based on Gender(Female)')
    presumptive_tested_positive__male = Field(attribute='presumptive_tested_positive__male', column_name='Presumptive who tested positive based on Gender(Male)')
    presumptive_tested_positive__female = Field(attribute='presumptive_tested_positive__female', column_name='Presumptive who tested positive based on Gender(Female)')

    class Meta:
        model = PresumptiveGenderDistribution
        exclude = ('is_active', 'modified_at', 'created_by', 'created_at', 'modified_by')

class PresumptiveCasesTestedStateResource(resources.ModelResource):
    id = Field(attribute='id', column_name='Id')

    class Meta:
        model = PresumptiveCasesTestedState
        exclude = ('is_active', 'modified_at', 'created_by', 'created_at', 'modified_by')

