from import_export import resources
from import_export.fields import Field
from .models import FollowUpStatistics


class FollowUpStatisticsResource(resources.ModelResource):
     id = Field(attribute='id', column_name='Id')
     called_back = Field(attribute='called_back', column_name='Presumptive cases called back')
     responded = Field(attribute='responded', column_name='Presumptive cases responded (reached?)')
     disclosed_not_tested = Field(attribute='called_back', column_name='Presumptive cases reached who disclosed not tested')
     disclosed_tested = Field(attribute='called_back', column_name='Presumptive cases reached who disclosed tested')
     disclosed_result = Field(attribute='called_back', column_name='Presumptive cases reached who did not disclose result')
     disclosed_positive = Field(attribute='called_back', column_name='Presumptive cases reached who disclosed Positive')
     disclosed_negative = Field(attribute='called_back', column_name='Presumptive cases reached who disclosed Negative')
     gotten_result = Field(attribute='called_back', column_name='Presumptive cases reached who has not gotten result')
     class Meta:
         model = FollowUpStatistics
         fields = ('id', 'called_back', 'responded', 'disclosed_not_tested','disclosed_tested','disclosed_result',
                   'disclosed_positive','disclosed_negative','gotten_result')
